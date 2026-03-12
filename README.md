# 🃏 MTG Planechase Discord Bot 🃏

A lightweight Discord bot that brings [Planechase](https://mtg.fandom.com/wiki/Planechase) to your Magic: The Gathering games. Roll the planar die right in your server planeswalk to random planes, trigger chaos abilities, or hit a blank.

Plane cards are pulled live from [Scryfall](https://scryfall.com/).

![Discord](https://img.shields.io/badge/Discord-bot-5865F2?logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## Commands

| Command | Description |
|---------|-------------|
| `/roll` | Roll the planar die |

### Die results

- **Planeswalker symbol** (1 in 6) — Planeswalk - A random plane or phenomenon is fetched from Scryfall and displayed.
- **Chaos symbol** (1 in 6) — Chaos ensues - Trigger the chaos ability of the current plane.
- **Blank** (4 in 6) — Nothing happens.

## Setup

### 1. Create a Discord bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application and add a bot.
3. Copy the bot token.

### 2. Install & run

```bash
git clone https://github.com/nsluke/Planechase-Bot.git
cd Planechase-Bot

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file (see `.env.example`):

```
PLANECHASE_BOT_TOKEN=your-discord-bot-token-here
```

Then run:

```bash
export PLANECHASE_BOT_TOKEN=$(cat .env | grep PLANECHASE_BOT_TOKEN | cut -d '=' -f2)
python planechase_bot.py
```

### 3. Invite the bot

Generate an invite link in the Developer Portal under *OAuth2 → URL Generator*.
Select the **bot** and **applications.commands** scopes, and these bot permissions:

- Send Messages
- Embed Links

## How it works

The bot uses the [Scryfall API](https://scryfall.com/docs/api) to fetch random plane and phenomenon cards. When a player rolls a planeswalk, a card embed is posted with the plane's artwork and a link to the full card on Scryfall.

## License

[MIT](LICENSE)
