import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please say something:")
    # Adjust for ambient noise and record
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Sorry, the service is unavailable.")
