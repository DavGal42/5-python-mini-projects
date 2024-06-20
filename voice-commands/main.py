"""
    Author: David Galstyan

    Description: This is a script which executes voice commands.
"""

import speech_recognition as sr
import os

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say 'Print text(your text)'")
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen to the input from the user
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)

            # Convert recognized text to a print statement
            if "print" in text.lower():
                statement = text.replace("print", "").strip()
                print_code = f'print("{statement}")'
                print(f"Generated code: {print_code}")

                # Execute the generated print statement
                exec(print_code)
            else:
                print("The text don't contain command print")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")

if __name__ == "__main__":
    main()
