# Tiff Discord Bot

Tiff is a modular Discord bot built with `discord.py`, focused on moderation utilities and hybrid commands (prefix + slash).

## AI Disclosure

This project was primarily developed by the author, with a small percentage of AI assistance during implementation and iteration. The README, however, was fully generated with AI.

## Features

- Hybrid commands (`prefix` and `/slash`) for core actions
- Moderation commands:
- `kick`
- `ban`
- `mute`
- `unmute`
- Utility command:
- `ping` (latency check)
- Owner-only command:
- `syncSlash` to sync application commands (global or test server)
- Safety checks for moderation actions:
- Prevent self-target actions
- Prevent actions against server owner
- Enforce role hierarchy for moderator and bot
- Centralized error handling for Discord permission/HTTP failures
- Configurable muted role and development guild via `config.toml`

## Tech Stack

- Python 3.11+
- `discord.py==2.6.0`
- `python-dotenv==1.0.0`

## Project Structure

```text
.
|-- main.py
|-- requirements.txt
|-- config.toml
|-- cogs/
|   |-- moderation/
|   |-- fun/
|   `-- owner_only/
|-- Helpers/
`-- Config/
```

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create your own `.env` file in the project root and add your bot credentials.

Example `.env`:

```env
TOKEN=your_discord_bot_token_here
PREFIX=$
GUILD_ID=your_development_guild_id_here
```

Important:
- You must create this `.env` file yourself.
- Replace `TOKEN` with your real Discord bot token.
- `GUILD_ID` is used by the `syncSlash ts` option for development sync.

5. Configure `config.toml`:
- `Server.Guild_Id` should be your development guild ID (integer).
- `Roles.Muted` should match the muted role name in your server.

6. Run the bot:

```bash
python main.py
```

## Commands

- `ping`: Replies with bot latency
- `kick <member> [reason]`: Kicks a member
- `ban <member> [reason]`: Bans a member
- `mute <member> [reason]`: Adds muted role
- `unmute <member> [reason]`: Removes muted role
- `syncSlash global`: Sync slash commands globally (owner only)
- `syncSlash ts`: Sync slash commands to test server (owner only)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
