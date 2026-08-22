from __future__ import annotations

import os

from hozan.core.app.application import Hozan


def main() -> None:
    """Start Hozan with the token configured in the environment."""
    token = os.environ["HOZAN_TOKEN"]
    Hozan(token).run()


if __name__ == "__main__":
    main()