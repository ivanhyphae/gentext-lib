import datetime as dt

import pytest
from pydantic import ValidationError

from gentext import inventory as inv


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
