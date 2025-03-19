# Keylogger Script

This Python script logs all keystrokes and records the active window where each key was pressed. The log is saved in a file named `log.txt`.

## 🛠 Requirements
Before running the script, install the required Python libraries:
```sh
pip install pynput
pip install pywin32
```

## 🚀 How It Works
1. The script listens for every key press.
2. It retrieves the currently active window title.
3. If the active window changes, it logs the new window title and timestamp.
4. Each key pressed is recorded in the `log.txt` file.
5. Special keys (such as `Enter`, `Shift`, etc.) are enclosed in brackets (`[ ]`).

## 📜 Code Explanation
- **`pressed_key(key)`**: Handles keypress events and writes them to `log.txt`.
- **`GetWindowText(GetForegroundWindow())`**: Gets the title of the active window.
- **`keyboard.Listener(on_press=pressed_key)`**: Starts a listener to monitor keystrokes.
- **`listener.join()`**: Keeps the script running indefinitely.

## 📂 Log File Example (`log.txt`)
```
#### Notepad - 2025-03-19 14:23:10
H e l l o   [Enter]
#### Browser - 2025-03-19 14:24:05
w w w . g o o g l e . c o m [Enter]
```

## 🏁 Running the Script
Simply execute the script:
```sh
python keylogger.py
```

## ⚠ Disclaimer
Use this script only in controlled environments such as penetration testing labs, with explicit permission. Misuse of this tool for unauthorized access to systems is illegal and may result in severe consequences. The risk is yours.


