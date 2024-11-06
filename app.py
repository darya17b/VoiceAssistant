import streamlit as st 

from audio_recorder_streamlit import audio_recorder
import openai
import base64

def main():
    st.sidebar.title("API KEY CONFIGURATION")
    api_key = st.sidebar.text_input("Please enter your API key!: ", type = "password") # could remove and include my api key

    st.title("AI Voice Assistant")
    st.write("Click on the voice recorder and tell me a prompt, I'll respond!")