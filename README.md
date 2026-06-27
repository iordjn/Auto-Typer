# Random Interval Keystroke Automator

A lightweight Python script that utilizes `pyautogui` to simulate realistic, human-like typing by introducing randomized delays between individual keystrokes. 

## Motivation
Have you ever encountered a website or an online form that frustratingly blocks you from pasting text? 
Getting tired of dealing with restrictive sites that disable the standard `Ctrl+V` / `Cmd+V` functionality, this script was quickly spun up to bypass those limitations. 
By pasting the restricted content directly into the script's string variable, the tool automatically types it out for you character-by-character, seamlessly side-stepping the block.

## Features
- **Humanized Typing Rhythm:** Instead of a uniform typing speed, the script pauses for a random duration between every character using `random.uniform()`.
- **Startup Delay:** Includes a configurable safety buffer (default: 3 seconds) allowing you to switch focus to the target text field or window before typing initiates.
- **Cross-Platform:** Works on Windows, macOS, and Linux wherever Python and PyAutoGUI are supported.

## Installation

1. **Clone or download** this repository to your local machine.
2. **Install the dependencies** using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
Note for Linux Users: pyautogui may require additional system packages such as scrot,
tk-dev, or python3-tk. If you run into issues, install them via your package manager (e.g.,
 sudo apt-get install python3-tk python3-dev).

Usage
Open the script and modify the letter variable with the string you want to type:

Python
```Python
letter = "I want to write this"
```
Run the script:

Bash
```bash
python script.py
```
Quickly click into the target text input, text editor, or application window during the 3-second countdown buffer.

Configuration
You can easily adjust the typing speed and variation by altering the parameters inside the random.uniform() function:

Python
# Faster, more frantic typing
random_interval = random.uniform(0.02, 0.15)

# Slower, highly deliberate typing
random_interval = random.uniform(0.10, 0.45)
Disclaimer
This script is intended for educational and automated testing purposes. Always ensure compliance with the terms of service of any application or platform where this script is executed.
