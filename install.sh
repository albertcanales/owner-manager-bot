#!/bin/bash

## Script that automatically installs owner-manager-bot
# Usage: ./install.sh TOKEN_FILE

SOURCE_HTTP="https://github.com/canales2002/owner-manager-bot.git"
TARGET_PATH="/opt/owner-manager-bot/"
BIN_PATH="/usr/local/bin/"
LOG_FILE="/var/log/owner-manager-bot.log"
SYSTEMD_PATH="/etc/systemd/system"

# Error Handling
set -e
trap 'error_handle $? $LINENO' EXIT
error_handle() {
    if [ "$1" != "0" ]; then
        # error handling goes here
        echo "Error $1 occurred on line $2."
    fi
}

if $# -lt 1; then
    echo "Usage: ./install.sh TOKEN_FILE"
    echo "Error: No token file was given"
fi

# Installation

echo "Downloading from source at $TARGET_PATH ..."
git clone "$SOURCE_HTTP" "$TARGET_PATH"

echo "Copying token ..."
cp $1 "$TARGET_PATH/token.txt"

ENV_PATH="$TARGET_PATH/env"
echo "Installing Python dependencies at $ENV_PATH ..."
python3 -m venv $ENV_PATH
"$ENV_PATH/bin/pip" install -r "$TARGET_PATH/requirements.txt"

echo "Creating executable file at $BIN_PATH ..."
cat > "$TARGET_PATH/owner-manager-bot" << ENDOFFILE
#!/bin/bash
$ENV_PATH/bin/python $TARGET_PATH/bot.py > "$LOG_FILE"
ENDOFFILE
chmod +x "$TARGET_PATH/owner-manager-bot"
ln -s "$TARGET_PATH/owner-manager-bot" "$BIN_PATH/owner-manager-bot"

echo "Creating Systemd Unit at $SYSTEMD_PATH ..."
cat > "$TARGET_PATH/owner-manager-bot.service" << ENDOFFILE
# owner-manager-bot
[Unit]
Description=Telegram bot for managing ownership of various items
After=network.target

[Service]
WorkingDirectory=$TARGET_PATH
ExecStart=owner-manager-bot

[Install]
WantedBy=multi-user.target
ENDOFFILE
ln -s "$TARGET_PATH/owner-manager-bot.service" "$SYSTEMD_PATH/owner-manager-bot.service"
systemctl daemon-reload
systemctl start owner-manager-bot
systemctl enable owner-manager-bot

