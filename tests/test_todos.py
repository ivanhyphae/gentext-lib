import datetime as dt

import pytest
from pydantic import ValidationError

from adapt_rfp import todos


def _todo(**kw):
    base = dict(id="t-001", title="X", kind="decision", venue="partner-meeting", topic="scope", priority=1,
                ask=["arpd"], context="c", added={"date": dt.date(2026, 9, 26), "by": "t"})
    base.update(kw)
    return base


def test_repo_todos_validate():
    tl = todos.load()
    assert tl.todos
    assert todos.uncovered_tk() == [], "every TK note in an answer draft should cite a todo id"


def test_closed_needs_resolution():
    with pytest.raises(ValidationError):
        todos.Todo(**_todo(status="answered"))
    todos.Todo(**_todo(status="answered", resolution={"date": dt.date(2026, 10, 1), "decided_by": ["arpd"], "text": "ok"}))


def test_meeting_items_need_ask():
    with pytest.raises(ValidationError):
        todos.Todo(**_todo(ask=[]))
    todos.Todo(**_todo(venue="internal", ask=[]))


def test_ids_unique_and_deps_known():
    with pytest.raises(ValidationError):
        todos.TodoList(todos=[_todo(), _todo()])
    with pytest.raises(ValidationError):
        todos.TodoList(todos=[_todo(depends_on=["t-009"])])
    assert todos.TodoList(todos=[_todo(), _todo(id="t-007")]).next_id() == "t-008"


def test_agenda_only_open_meeting_items():
    tl = todos.TodoList(todos=[
        _todo(),
        _todo(id="t-002", venue="internal", ask=[]),
        _todo(id="t-003", status="done", resolution={"date": dt.date(2026, 10, 1), "decided_by": ["x"], "text": "y"}),
    ])
    md = todos.render_agenda(tl)
    assert "t-001" in md and "t-002" not in md and "t-003" not in md
