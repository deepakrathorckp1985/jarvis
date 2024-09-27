import streamlit as st
import requests

def get_mistral_respons(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input':{'topic':input_text}})
    
    return response.json()['output']


st.title("API testing with mistral LLM model")
input_text = st.text_input("Write a poem on")

if input_text:
    st.write(get_mistral_respons(input_text))