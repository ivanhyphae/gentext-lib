import json

import pytest

from gentext import card, profile
from gentext.extract import redact


def test_markdown_sections_and_trail():
    body = " ".join(["word"] * 40)
    text = f"intro line\n# Overview\n{body}\n## Site\n{body}\n# Notes\n{body}\n"
    secs = profile.split_sections(text, markdown=True)
    paths = [s.path for s in secs]
    assert "Overview > Site" in paths and "Notes" in paths
    assert next(s for s in secs if s.path == "Overview > Site").words == 40


def test_fallback_parts_when_no_headings():
    text = " ".join(["word"] * 1500)
    secs = profile.split_sections(text, markdown=False)
    assert [s.path for s in secs] == ["part 1", "part 2", "part 3"]


def test_shingles_detect_containment():
    base = " ".join(f"w{i}" for i in range(300))
    bigger = base + " " + " ".join(f"x{i}" for i in range(300))
    a, b = profile.shingles(base), profile.shingles(bigger)
    assert len(a & b) / len(a) > 0.95


def test_redact():
    assert redact("Call 925-555-1212 or mail jo@example.org") == "Call [phone] or mail [email]"


def test_card_schema_is_strict():
    schema = card._schema()

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "object":
                assert node["additionalProperties"] is False
                assert set(node["required"]) == set(node["properties"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(schema)


GOOD = {
    "summary": "s", "doc_role": "guidance", "authorship": "LCI", "disposition": "reference",
    "disposition_reason": "r", "serves_needs": [{"need_id": "hr-q2", "how": "h"}],
    "sections": [{"path": "A", "type": "method", "reuse_value": "high", "note": "n"}],
    "fact_candidates": [], "flags": [],
}


def test_ingest_validates(tmp_path, monkeypatch):
    monkeypatch.setattr(card, "PROMPT_DIR", tmp_path / "prompts")
    monkeypatch.setattr(card, "CARD_DIR", tmp_path / "cards")
    card.PROMPT_DIR.mkdir()
    for aid in ("good", "bad"):
        (card.PROMPT_DIR / f"{aid}.json").write_text(json.dumps({"text_sha256": "x"}))
    ok, errors = card.ingest({"good": GOOD, "bad": {**GOOD, "disposition": "keep-forever"}})
    assert ok == ["good"] and "bad" in errors
    assert (card.CARD_DIR / "good.yaml").exists()


def test_needs_text_lists_questions():
    txt = card.needs_text()
    assert "hr-q1" in txt and "ambrose-memorial-park" in txt
