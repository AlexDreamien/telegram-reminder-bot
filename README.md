# telegram-reminder-bot

A personal Telegram reminder bot: set one-off and recurring reminders through an inline
menu, and the bot delivers them on time. Built with aiogram 3, APScheduler, and SQLite.

_Screenshot of the conversation will be added once the bot has been deployed._

## Features

- Inline menu — add, list, and delete reminders without typing commands.
- Relative time (`in 2 hours`, `in 30 minutes`) and absolute time (`2026-05-14 18:30`).
- Recurring reminders: daily and weekly.
- Paginated list of active reminders.
- Reminders survive restarts: jobs are re-scheduled from SQLite on startup.

## Installation

```bash
git clone https://github.com/AlexDreamien/telegram-reminder-bot.git
cd telegram-reminder-bot
python -m venv .venv
.venv\Scripts\activate           # Windows
# source .venv/bin/activate      # macOS / Linux
pip install -r requirements.txt
cp .env.example .env             # then edit .env and set BOT_TOKEN
python main.py
```

Obtain `BOT_TOKEN` from [@BotFather](https://t.me/BotFather).

## Usage

Send `/start` to the bot and use the inline menu. `/help` lists all commands.

## Tech stack

- Python 3.11+
- [aiogram 3](https://docs.aiogram.dev/) — Telegram bot framework
- [APScheduler](https://apscheduler.readthedocs.io/) — job scheduling
- SQLite — persistent storage
- pytest, ruff, black

## Testing

```bash
pip install -r requirements-dev.txt
pytest
ruff check .
black --check .
```

CI runs the same checks on every push (see `.github/workflows/ci.yml`).

## License

[MIT](LICENSE)
