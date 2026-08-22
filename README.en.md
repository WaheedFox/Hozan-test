# Hozan

Hozan is a simple and modern no-code platform for building Telegram bots with
Titan.

## Usage

Set the bot token in `HOZAN_TOKEN`, then run:

```bash
hozan
```

You can also start Hozan from Python:

```python
from hozan import Hozan

app = Hozan("your-telegram-bot-token")
app.run()
```