"""
    Description: This is a script which executes voice commands.
"""

import os
import time
import speech_recognition


def set_timer(seconds):
    """
        Description: Set n second timer
        Arguments: Seconds
    """
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1


def open_file(filename):
    """
        Description: Open new file
        Arguments: File name
    """
    with open(filename, 'w', encoding='UTF-8'):
        pass

def create_html_file(filename):
    """
        Description: Create HTML file
        Arguments: File name
    """
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(html_content)


def start_code():
    """
        Description: Function with commands
    """
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Say something")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        lower_text = text.lower()
        if "print" in lower_text:
            text = lower_text.replace("print", "").strip()
            print(text)

        elif "open google chrome" in lower_text:
            os.system("start chrome")

        elif "set timer" in lower_text:
            try:
                seconds = int(lower_text.split("set timer for ")[1].split(" seconds")[0])
                set_timer(seconds)

            except (IndexError, ValueError):
                print("You should say:'Set timer for n seconds'")

        elif "open file" in lower_text:
            try:
                filename = text.split("open file ")[1]
                open_file(filename)
            except IndexError:
                print("You should say:'Open file filename'")

        elif "create html file" in lower_text:
            try:
                filename = lower_text.split("create html file ")[1].strip()
                create_html_file(filename)
            except IndexError:
                print("You should say:'Create html file filename'")

        else:
            print("There is no such command")

    except speech_recognition.UnknownValueError:
        print("Speech Recognition could not understand the command")


def main():
    """
        The main function
    """
    start_code()


if __name__ == "__main__":
    main()
