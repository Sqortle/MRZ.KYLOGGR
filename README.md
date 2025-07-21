# Keylogger with Email Reporting

This Python script records the user's keystrokes and sends them via email at regular intervals (e.g., every 30 seconds).

## Features

- Logs all keystrokes in real time.
- Handles special keys like `backspace`, `space`, and `enter`.
- Sends the captured keystrokes via email every 30 seconds.

## Requirements

Python 3.6 or higher

### Required Libraries:

```bash
pip install pynput
```

## Usage

1. Replace `<EMAIL>` and `"password"` in the script with your own Gmail address and **App Password**.
2. Make sure **2-Step Verification** is enabled on your Gmail account and generate an **App Password**.
3. Run the script with:

```bash
python keylogger.py
```

## ⚠️ Disclaimer

❗ This script is for **educational purposes only**. Unauthorized use may be considered **illegal** depending on your local laws. Use only on your own devices for testing and learning purposes.
