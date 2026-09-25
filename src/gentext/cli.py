import argparse
import json
import sys
from pathlib import Path


def _inventory(args: argparse.Namespace) -> int:
    from pydantic import ValidationError

    from gentext import inventory as inv_mod

    try:
        inv = inv_mod.load()
    except ValidationError as e:
        print(e, file=sys.stderr)
        return 1

    if args.inv_cmd == "validate":
        print(f"ok: {len(inv.assets)} assets, {len(inv.sweeps)} sweeps")
        return 0
    if args.inv_cmd == "index":
        inv_mod.INDEX_FILE.write_text(inv_mod.render_index(inv))
        print(f"wrote {inv_mod.INDEX_FILE}")
        return 0
    if args.inv_cmd == "find":
        hit = inv.find_source(args.system, args.source_id)
        print(json.dumps(hit.model_dump(mode="json") if hit else None, indent=2))
        return 0 if hit else 3
    if args.inv_cmd == "list":
        for a in inv.assets:
            if args.status and a.status != args.status:
                continue
            print(f"{a.priority or '-'}\t{a.status}\t{a.id}\t{a.title}")
        return 0
    if args.inv_cmd == "upsert":
        import yaml as _yaml

        records = _yaml.safe_load(Path(args.file).read_text())
        if isinstance(records, dict):
            records = [records]
        try:
            added, updated = inv_mod.upsert(records)
        except (ValidationError, ValueError) as e:
            print(e, file=sys.stderr)
            return 1
        print(f"added {len(added)}: {added}\nupdated {len(updated)}: {updated}")
        return 0
    if args.inv_cmd == "hash":
        print(inv_mod.sha256(Path(args.path)))
        return 0
    return 2


def _select(ids: list[str], status: list[str] | None) -> list:
    from gentext import inventory as inv_mod

    assets = [a for a in inv_mod.load().assets if a.local]
    if ids:
        assets = [a for a in assets if a.id in ids]
    if status:
        assets = [a for a in assets if a.status in status]
    return assets


def _profile(args: argparse.Namespace) -> int:
    from gentext import profile

    profs = profile.profile_assets(_select([], None))  # always across all, for duplicate detection
    print(f"profiled {len(profs)} assets -> {profile.PROFILE_DIR}")
    return 0


def _card(args: argparse.Namespace) -> int:
    from gentext import card

    assets = _select(args.ids, None)
    if args.card_cmd == "run":
        entry = card.run_api(assets, batch=not args.sync, force=args.force)
        print(json.dumps(entry, indent=2, default=str))
        return 0 if not entry.get("errors") else 1
    if args.card_cmd == "prepare":
        n = card.prepare(assets, force=args.force)
        print(f"wrote {n} prompt files to {card.PROMPT_DIR}")
        return 0
    if args.card_cmd == "ingest":
        ok, errors = card.ingest(json.loads(Path(args.file).read_text()))
        print(f"saved {len(ok)} cards; errors: {errors}")
        return 0 if not errors else 1
    if args.card_cmd == "show-prompt":
        system, todo = card.plan(assets, force=True)
        print(system if args.system else "\n\n".join(u for _, u, _ in todo))
        return 0
    return 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="gentext")
    parser.add_argument("--version", action="store_true")
    sub = parser.add_subparsers(dest="cmd")

    p_inv = sub.add_parser("inventory", help="asset discovery/acquisition manifest (DR-0010)")
    inv_sub = p_inv.add_subparsers(dest="inv_cmd", required=True)
    inv_sub.add_parser("validate", help="validate inventory/assets.yaml and sweeps.yaml")
    inv_sub.add_parser("index", help="regenerate inventory/index.md")
    p_find = inv_sub.add_parser("find", help="look up an asset by source-system id (dedup check)")
    p_find.add_argument("system")
    p_find.add_argument("source_id")
    p_list = inv_sub.add_parser("list", help="list assets")
    p_list.add_argument("--status")
    p_up = inv_sub.add_parser("upsert", help="add/update records from a YAML file (merge by id, keeps comments)")
    p_up.add_argument("file")
    p_hash = inv_sub.add_parser("hash", help="sha256 of a local file (for `local.sha256`)")
    p_hash.add_argument("path")

    sub.add_parser("profile", help="T1: outline, sizes, contact counts, near-duplicates for all acquired assets (DR-0011)")
    p_card = sub.add_parser("card", help="T2: Haiku cards with dispositions (DR-0011)")
    card_sub = p_card.add_subparsers(dest="card_cmd", required=True)
    for name, hlp in [("run", "call the Anthropic API (Batch by default; needs ANTHROPIC_API_KEY, e.g. uv run --env-file .env)"),
                      ("prepare", "subagent backend: write prompt files to build/card-prompts/"),
                      ("show-prompt", "print the user prompt(s), or --system")]:
        sp = card_sub.add_parser(name, help=hlp)
        sp.add_argument("ids", nargs="*", help="asset ids (default: all acquired)")
        sp.add_argument("--force", action="store_true", help="re-card even if the card is current")
        if name == "run":
            sp.add_argument("--sync", action="store_true", help="one request at a time instead of the Batch API")
        if name == "show-prompt":
            sp.add_argument("--system", action="store_true")
    p_ing = card_sub.add_parser("ingest", help="subagent backend: validate and save {asset_id: card} JSON")
    p_ing.add_argument("file")

    args = parser.parse_args(argv)
    if args.version:
        from importlib.metadata import version

        print(version("gentext"))
        return 0
    if args.cmd == "inventory":
        return _inventory(args)
    if args.cmd == "profile":
        return _profile(args)
    if args.cmd == "card":
        return _card(args)
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
