from hozan.core.app.application import Hozan


def test_hozan_creates_a_titan_bot(monkeypatch):
    created = []

    class FakeTitan:
        def __init__(self, token):
            created.append(token)

    monkeypatch.setattr(
        "hozan.core.app.application.Titan",
        FakeTitan,
    )

    app = Hozan("test-token")

    assert isinstance(app.bot, FakeTitan)
    assert created == ["test-token"]