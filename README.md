# Chatwork AI Bot (Local-first Upgrade)

This repository now includes a safer local-first bot response layer that can be tested
without external API credentials. The legacy API script is preserved in `legacy/`.

## Features

- Local response engine with simple intent routing
- CLI for rapid testing (`--message`)
- API handler wrapper for deployment-style environments
- Unit tests for response behavior and CLI flow

## Usage

```bash
python3 cli.py --message "deploy update needed"
```

## Run Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Notes

- Original integration script remains at `legacy/api/chatwork_bot.py`.
- You can rewire `api/chatwork_bot.py` to external providers later.

## License

MIT License. See `LICENSE`.
