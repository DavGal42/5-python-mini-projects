## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Telegram-Animated-Emojis/main/Travel%20and%20Places/Rocket.webp" alt="Rocket" width="30" height="30" /> Installation Guide

### 1. Create Virtual Environment

```bash
python -m venv myvenv
```

### 2. Activate Virtual Environment

- Linux / macOS (bash/zsh):
```bash
source myvenv/bin/activate
```

- Windows (PowerShell):
```powershell
.\myvenv\Scripts\Activate.ps1
```

- Windows (cmd):
```powershell
myvenv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Adjust Code for Linux Users

If you are running the script on Linux, go to line 68 in main.py and replace:
```python
os.system("start chrome")
```

with:
```python
os.system("google-chrome &")
```

### 5. Run the Script

```bash
python .\main.py
```

#### **<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Telegram-Animated-Emojis/main/Objects/Microphone.webp" alt="Microphone" width="30" height="30" /> Available Voice Commands**

When the script is running and you see Say something, you can use these voice commands:

- Open Google Chrome
    
  → Launches Chrome browser.
  (Linux users must adjust the code as explained above).

- Set timer for N seconds
    
  Example:
  Set timer for 10 seconds
  
  → Starts a countdown timer.

- Open file filename
  
  Example:
  Open file notes.txt
  
  → Opens the specified file if it exists.

- Create html file filename
    
  Example:
  Create html file index.html

  → Creates a new HTML file with the given name.

**If the command is not recognized, the program will print:
There is no such command**

### 6. Deactivate Virtual Environment

```bash
deactivate
```
