

# 🛡️ KeyLogger Basic – Educational Keylogging Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> **Created by Usman Balogun Temitope(a.k.a. Dollarhunter)**  
> For **educational and ethical hacking purposes only**.

---

## 📌 Overview

**KeyLogger Basic** is a simple, lightweight Python tool that logs:

- 👨‍💻 Keystrokes
- 📋 Clipboard activity
- 🖼️ Screenshots at regular intervals

It is designed for **ethical hacking training**, **parental monitoring**, and **Python cybersecurity education**.

> ⚠️ Use this software **only** on devices you own or have explicit permission to monitor.

---

## 📁 Features

- ✅ Logs all keystrokes to a file (`keylog.txt`)
- 📋 Tracks clipboard data and saves to `clipboard_log.txt`
- 🖼️ Takes a screenshot every 60 seconds into the `screenshots/` folder
- ⏱️ Timestamps for clipboard and screenshots
- 🔄 Runs everything concurrently using `threading`
- 💻 Runs silently in the background

---

## 🧾 How It Works

Your Python script has 3 main background tasks:

| Task            | File/Output                  | Interval  |
|-----------------|------------------------------|-----------|
| Keystroke log   | `keylog.txt`                 | Instant   |
| Clipboard log   | `clipboard_log.txt`          | Every 5s  |
| Screenshot log  | `screenshots/YYYY-MM-DD_*.png` | Every 60s |

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python 3.8 or higher installed.  
Then install the required libraries:

```bash
pip install pynput Pillow pyperclip
````

### 📂 File Structure

```
keylogger/
├── keylogger.py
├── keylog.txt
├── clipboard_log.txt
└── screenshots/
```

---

## ▶️ How to Run

1. Clone the repository or download the script
2. Open a terminal and run the script:

```bash
python keylogger.py
```

The script will begin:

* Listening for keypresses
* Saving new clipboard content
* Taking screenshots every 60 seconds

> All logs are saved locally in the same directory as the script.

---

## ⚠️ Legal Warning

> This tool is intended **only for educational use**, ethical hacking training, or parental control where applicable.

Using it on someone else's device **without permission** is **illegal** in many countries.

**The author takes no responsibility for any misuse.**

---

## 👨‍💻 Author

**Balogun Usman Temitope**
Senior Backend Developer | Python Security Enthusiast
📍 Based in Nigeria
🔗 GitHub: [@dollarhunter](https://github.com/usmanbalogun044) 

---

## 💡 Tips for Improvement

* 🔒 Add encryption to logs
* ✉️ Send logs via email or webhook
* ⛔ Add self-destruct or stop key
* 🧪 Turn it into a `.pyw` background app on Windows
* 🪟 Auto-start on boot (advanced)

---

## ⭐ License

This project is licensed under the [MIT License](LICENSE).

