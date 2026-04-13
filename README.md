# Chatwork AI Bot (Local-first Upgrade)

<!-- BrandCloud:readme-standard -->
[![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Showcase](https://img.shields.io/badge/Portfolio-Showcase-blue.svg)](#)

_Part of the `sakib-maho` project showcase series with consistent documentation and quality standards._

This repository now includes a safer local-first bot response layer that can be tested
without external API credentials. The legacy API script is preserved in `legacy/`.

## Features

- Local response engine with simple intent routing
- CLI for rapid testing (`--message`)
- API handler wrapper for deployment-style environments
- Unit tests for response behavior and CLI flow

## Quick Start

```bash
python3 cli.py --message "deploy update needed"
```

## Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## License

MIT License. See `LICENSE`.

## Notes

- Original integration script remains at `legacy/api/chatwork_bot.py`.
- You can rewire `api/chatwork_bot.py` to external providers later.
