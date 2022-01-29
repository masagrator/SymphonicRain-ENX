# Symphonic Rain Translation Mod for Nintendo Switch

This is a port of official translation to Nintendo Switch version of game Symphonic Rain.
It works correctly only with version 1.0.0 since no update was released for this game when mod was finished.

It should work with both jailbroken Nintendo Switch and emulators.

---

# Important notes

Status: **Beta**

Game was tested following this walkthrough:
https://forums.fuwanovel.net/topic/2430-symphonic-rain/

By following it and passing positively all minigames you have 100% warranty that you won't meet any crash, text going out of bounds, and other glitches related to this mod.
Minigames can be avoided by forcing game to play them for you in settings.
Walkthrough is using fantranslation lines which are almost never 1:1 with official translation, but it's understandable enough to not get lost.

If you don't want to follow walkthrough, be sure to save at the beginning of each day inside game (not quick save), this will help you skip game back to where you have ended in case of meeting unexpected glitch that can crash game or make it stuck in infinite loop.

If you will find any issue, provide screenshot of text that is causing issue and post it in [Issues](https://github.com/masagrator/SymphonicRain-ENX/issues). Before crash (which is predictable because of sound thread being terminated aka background sounds stop suddenly) you have few seconds to make screenshot before app will close.

Some text blocks in ADV mode had more than 4 lines which is not something game supports. Part of them were voiced messages. 
Voice file is stopped when you're switching to next page of text, that's why in case of 5-line messages You will see only 4 lines of message when voice is played and 5th line is available in next page without voice file.

Game engine has issues with timers which is not because of mod, f.e. lyrics which are showed few seconds earlier than they should.

Don't update mod if it's not necessary. If next updates changed commands blob related to your save, it may not be usable anymore.

---

# Technical Notes

- Disassembler and assembler were made based on debug notes inside game executable
- Patch is making font smaller to fit more text
- Engine was adjusted to render only 3 lines in ADV mode:
  - 3rd line cannot go over the space dedicated to book icon otherwise game will crash (this means averagely ASCII 52 characters max)
  - 4th line cannot have more than 25 glyphs otherwise game will crash or stuck in infinite loop
- When game is using WAIT command, it adds additional space between next messages if they are rendered next to each other. Issue is this happens only in ADV window and with disabled skipping. In backlog this space is not saved. That's why I was trying to implement in those places hardcoded spaces where they were needed, which in normal play speed results in rendering those lines with wider space than necessary.
- Engine by default renders glyphs at fixed width for any character outside of ASCII table. Patch blocks this feature for all characters.
- Patch also changes date format in saves to match Steam version.

---

# How to
Install mod for Nintendo Switch:
- Download newest release [HERE](https://github.com/masagrator/SymphonicRain-ENX/releases) or latest artifacts from [HERE](https://github.com/masagrator/SymphonicRain-ENX/actions) (github account is required, assets and scenario must be downloaded separately).
  - Release: Put "atmosphere" folder to the root of your sdcard
  - Artifacts: Put "contents" and "exefs_patches" folders inside "atmosphere" folder on your sdcard
- Play game

For emulators go to each dedicated to them Discords for support about installing mods.

About building mod yourself, check github workflows available in this repo.

---

# Additional Notes

- Translation mod is based on Steam release of the same game: https://store.steampowered.com/app/629650/Symphonic_Rain/
- Scenario is identical in both Nintendo Switch and Steam versions

---

# Thanks to:

- Original English translators of Symphonic Rain Steam version
- [aboood40091](https://github.com/aboood40091) for [BNTX-Injector](https://github.com/aboood40091/BNTX-Injector)
