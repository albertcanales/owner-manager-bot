A Telegram Bot that manages the ownership of some items in a group. You can try it at `@owner_manager_bot`.

## Summary

Once in a group, the bot accepts the following commands:
- `/help`: Shows available commands
- `/mkitem` item: Creates a new item with the sender as the owner
- `/rmitem` item: Removes the given item
- `/chown` item: Changes the ownership of item to the sender
- `/status`: Displays the owner of each item

A complete post about the development of this project will soon be available in [my webpage](albertcanales.com/blog).

## Installation

The script `install.sh` automatically installs the bot, its dependencies and enables its systemd service.

If you don't want to do any changes, you can use the following one-liner for the installation:

```
wget -qO - https://raw.githubusercontent.com/canales2002/owner-manager-bot/main/install.sh | sudo bash
```

## Suggestions

Any suggestion, bug report or improvement is gladly welcome. You can contact me via the email provided in my webpage.

Thank you for passing by!


