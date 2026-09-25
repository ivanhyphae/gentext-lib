import datetime as dt

import pytest
from pydantic import ValidationError

from adapt_rfp import inventory as inv


def _asset(**kw):
    base = dict(
        id="x",
        title="X",
        kind="proposal",
        status="discovered",
        location={"system": "gdrive", "id": "abc"},
        discovered={"date": dt.date(2026, 9, 25), "by": "t"},
    )
    base.update(kw)
    return base


def test_repo_inventory_validates():
    data = inv.load()
    assert data.assets, "inventory/assets.yaml should not be empty"


def test_wanted_needs_hint():
    with pytest.raises(ValidationError):
        inv.Asset(**_asset(status="wanted", location=None))
    inv.Asset(**_asset(status="wanted", location=None, hint="ask James"))


def test_acquired_needs_local():
    with pytest.raises(ValidationError):
        inv.Asset(**_asset(status="acquired"))
    inv.Asset(**_asset(status="acquired", local={"path": "sources/x.pdf"}))


def test_bad_slug_rejected():
    with pytest.raises(ValidationError):
        inv.Asset(**_asset(id="Not A Slug"))


def test_duplicate_source_ids_rejected():
    a = _asset(id="a")
    b = _asset(id="b")
    with pytest.raises(ValidationError):
        inv.Inventory(assets=[a, b])


def test_unknown_sweep_rejected():
    a = _asset(discovered={"date": dt.date(2026, 9, 25), "by": "t", "sweep": "nope"})
    with pytest.raises(ValidationError):
        inv.Inventory(assets=[a])


def test_find_source():
    data = inv.Inventory(assets=[_asset(id="a")])
    assert data.find_source("gdrive", "abc").id == "a"
    assert data.find_source("gdrive", "zzz") is None


def test_index_is_current():
    """inventory/index.md must be regenerated after editing assets.yaml."""
    assert inv.INDEX_FILE.read_text() == inv.render_index(inv.load())


def test_upsert_roundtrip(tmp_path):
    (tmp_path / "inventory").mkdir()
    (tmp_path / "inventory" / "assets.yaml").write_text(
        "# keep me\n- id: a\n  title: A\n  kind: proposal\n  status: discovered\n"
        "  location: {system: gdrive, id: abc}\n"
    )
    added, updated = inv.upsert(
        [{"id": "a", "status": "include", "priority": 1}, {"id": "b", "title": "B", "kind": "report", "status": "wanted", "hint": "ask"}],
        root=tmp_path,
    )
    assert added == ["b"] and updated == ["a"]
    text = (tmp_path / "inventory" / "assets.yaml").read_text()
    assert "# keep me" in text and "{system: gdrive, id: abc}" in text
    data = inv.load(tmp_path)
    assert data.assets[0].status == "include"


def test_upsert_rejects_invalid(tmp_path):
    (tmp_path / "inventory").mkdir()
    f = tmp_path / "inventory" / "assets.yaml"
    f.write_text("- id: a\n  title: A\n  kind: proposal\n  status: wanted\n  hint: h\n")
    with pytest.raises(ValidationError):
        inv.upsert([{"id": "a", "status": "acquired"}], root=tmp_path)
    assert "status: wanted" in f.read_text()
