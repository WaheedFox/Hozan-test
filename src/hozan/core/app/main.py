from future import annotations

import os

from hozan.core.app.application import Hozan

def main() -> None:
token = os.environ["HOZAN_TOKEN"]
Hozan(token).run()

if name == "main":
main()