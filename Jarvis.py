from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv
from translate import Translator


load_dotenv()

translator= Translator(to_lang="hi")

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
recognizer = sr.Recognizer()

def  recognize_speech():
    with sr.Microphone() as source:
        print("Please say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, the service is unavailable.")

def text_to_speech(text):
    tts = gTTS(text=text, lang='hi',slow='false')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    os.remove("output.mp3")

def get_llm_response(prompt):
    llm = Ollama(model="mistral")
    response = llm(prompt)
    return response



def start_program():
        user_input = recognize_speech()
        if user_input:
            response = get_llm_response(user_input)
            text_to_speech(response)

if __name__ == "__main__":
    start_program()