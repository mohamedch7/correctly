import os
import openai
import threading
from pynput import keyboard
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

typed_text = ""
last_key_timer = None

# Constants for QWERTY keyboard layouts (English and Arabic)
ENGLISH_LAYOUT = "qwertyuiop[]asdfghjkl;'\\zxcvbnm,./"
ARABIC_LAYOUT = "ضصثقفغعهخحجةشسيبلاتنمك؛\\ظطذدزرو،./"

# Detect and convert the wrong language layout using OpenAI
def convert_with_ai(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant that corrects text written with the wrong keyboard layout. The user's English layout is: {ENGLISH_LAYOUT} and their Arabic layout is: {ARABIC_LAYOUT}."},
                {"role": "user", "content": f"The following text was written with the wrong keyboard layout. Correct it to the intended English text:\n\n{text}\n\nCorrected:"}
            ],
            max_tokens=60,
            temperature=0.3
        )
        corrected_text = response['choices'][0]['message']['content'].strip()
        return corrected_text
    except Exception as e:
        print(f"Error with AI conversion: {e}")
        return text

# Handle language detection after a delay
def delayed_check():
    global typed_text
    corrected_text = convert_with_ai(typed_text)
    print(f"Original (wrong layout): {typed_text}")
    print(f"Corrected: {corrected_text}")
    # Reset the text buffer
    typed_text = ""

# Function to handle key presses
def on_press(key):
    global typed_text, last_key_timer

    try:
        # Append the typed character to the text buffer
        if key.char.isprintable():
            typed_text += key.char

        # Cancel any existing timer since we're still typing
        if last_key_timer is not None:
            last_key_timer.cancel()

    except AttributeError:
        # Handle special keys like space, backspace, etc.
        if key == keyboard.Key.space:
            typed_text += " "
        elif key == keyboard.Key.backspace and len(typed_text) > 0:
            typed_text = typed_text[:-1]

# Function to handle key releases
def on_release(key):
    global last_key_timer

    # Start or restart the timer to wait for 3 seconds after the last key release
    if last_key_timer is not None:
        last_key_timer.cancel()

    # Set a new timer for 3 seconds
    last_key_timer = threading.Timer(3.0, delayed_check)
    last_key_timer.start()

# Listener to capture key presses and releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
