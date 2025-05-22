import streamlit as st
from gtts import gTTS
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.playback import play
import openai

# Optional: Set your OpenAI API key here
openai.api_key = "your-openai-api-key"  # Replace with your actual key

# Function to convert speech to text
def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Please speak now.")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand your voice."
        except sr.RequestError:
            return "API unavailable."

# Function to get GPT response
def generate_response(prompt):
    if openai.api_key:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message["content"]
        except Exception as e:
            return f"Error with OpenAI API: {e}"
    else:
        return "OpenAI API key not set. This is a sample response."

# Function to convert text to speech and play it
def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    audio = AudioSegment.from_mp3("response.mp3")
    play(audio)

# Streamlit UI
st.set_page_config(page_title="AI Voice Bot", page_icon="🗣️")
st.title("🗣️ AI Voice Bot")

st.markdown("""
Speak into your mic. The bot will understand you, generate a response using AI, and reply with speech.
""")

if st.button("🎤 Speak Now"):
    user_text = transcribe_audio()
    st.success(f"You said: {user_text}")

    response = generate_response(user_text)
    st.info(f"🤖 Bot: {response}")

    speak_text(response)
