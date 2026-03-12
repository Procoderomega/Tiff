# Changelog

## Unreleased
### Working on
- Log system
- New modularization approach
- New metaclass methods for services

## 1.14.3
### Changed
- Fixed `logging_service` bug in ban.py

### Added 
- Added `logging_service` to mute.py
- Added `log_mute` function in `logging_service.py`

---

## 1.14.0
### Added
- Added `services/` folder
- Added `__init__.py` to `services/`
- Added `logging_service.py`
- `LoggingService` initialization in `main.py`

### Changed
- Testing logging service with `ban.py`

### Known Issues
- Ban command logging currently broken

---

## 1.13.0
### Added
- Added moods.json in Config/
- Added bot_mood.py in Fun/

## Changed
- Fixed bugs on sync_command.py

---

## 1.12.8
### Changed
- Renamed imported files in `cogs/moderation/init.py`

### Fixed
- Critical bug in `cogs/moderation/init.py` [When renaming the classes, I didn’t rename the imported files in init.py, which caused a critical bug.]

## 1.12.7
### Changed
- Added a metaclass function to all classes in my cogs, reducing lines of code and improving internal code readability
- Updated changelog.md
- Modified line 32 of main.py
- Renamed multiple classes in various moderation commands

---

## 1.12.3
### Added
- Ephemeral option for the `/pong` slash command in `pong.py`.
- Prefix configuration in `config.toml` — allows modifying the bot's prefix.
- Updated prefix extraction logic in `main.py`.

---

## 1.12.0
### Added
- Added `auto_init_meta.py` file to manage automatic Cog initialization


### Changed
- Started using metaclasses to reduce boilerplate and improve UX
- Updated `pong.py` to test MetaCog functionality

--- 

## 1.11.0
### Added
- README.md File - on root project
- Changelog.md File - on root project

--- 

## 1.10.0
### Added
- owner_only folder inside cogs
- automated sync helper

### Changed
- GID extraction now uses tomllib

### Removed
- global and test_server variables from main.py
