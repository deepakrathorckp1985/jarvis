from gtts import gTTS
import pygame
import os

def text_to_speech(text):
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en')
    # Save the converted speech to a file
    tts.save("output.mp3")
    
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the MP3 file
    pygame.mixer.music.load("output.mp3")
    # Play the file
    pygame.mixer.music.play()
    
    # Wait for the music to finish
    while pygame.mixer.music.get_busy():
        continue

    # Remove the file after playing
    os.remove("output.mp3")

# Get text input from the user
text = input("Enter text to convert to speech: ")
text_to_speech(text)
