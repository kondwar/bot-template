# Instructions for the AI assistant editing this repository

This is a Telegram bot built with Python and aiogram 3. Follow these rules for every change.

## Structure (flat, all files in the repo root)
- `bot.py`: entry point. Do NOT edit unless necessary. It auto-loads every `feature_*.py` file.
- `config.py`: reads environment variables. Add new variables here AND to `.env.example`.
- `feature_*.py`: one file per feature. Each must define `router = Router()`.
- `requirements.txt`: add every new dependency here.

## Rules
1. To add a feature, create a new `feature_<name>.py` file instead of editing existing ones.
2. Never hardcode tokens, API keys, or passwords. Use `settings.X` from `config.py`.
3. Never touch `.env`. Only update `.env.example` with empty placeholders.
4. Keep all handlers `async`. Handle errors with try/except and log them.
5. Reply to users in the language they write in.
6. When you add a required variable, list it in your answer so the owner can set it on the VPS.

## Output format
Return the full content of each created or changed file, with its path.
