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

    args = parser.parse_args(argv)
    if args.version:
        from importlib.metadata import version

        print(version("gentext"))
        return 0
    if args.cmd == "inventory":
        return _inventory(args)
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
