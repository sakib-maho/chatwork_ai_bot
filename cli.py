"""CLI simulation for Chatwork bot response flow."""

from __future__ import annotations

import argparse

from chatwork_bot.responder import build_local_response


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate local bot response for a message.")
    parser.add_argument("--message", required=True)
    args = parser.parse_args()
    print(build_local_response(args.message))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
