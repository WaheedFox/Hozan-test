from hozan.core.app.application import Hozan
from hozan.platform.telegram.application import TelegramApplication


def test_telegram_application_creates_a_titan_bot(monkeypatch):
    created = []

    class FakeTitan:
        def __init__(self, token):
            created.append(token)

    monkeypatch.setattr(
        "hozan.platform.telegram.application.Titan",
        FakeTitan,
    )

    app = TelegramApplication("test-token")

    assert isinstance(app.bot, FakeTitan)
    assert created == ["test-token"]


def test_hozan_uses_telegram_application(monkeypatch):
    included = []

    class FakeTelegramApplication:
        def __init__(self, token):
            self.bot = object()
            self.token = token

        def include(self, router):
            included.append(router)

        def run(self):
            pass

        async def start(self, lifecycle):
            pass

    monkeypatch.setattr(
        "hozan.core.app.application.TelegramApplication",
        FakeTelegramApplication,
    )

    app = Hozan("test-token")

    assert app.telegram.token == "test-token"
    assert app.bot is app.telegram.bot
    assert len(included) == 1