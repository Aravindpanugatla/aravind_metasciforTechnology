import streamlit as st
from gtts import gTTS
import os
from io import BytesIO
from tempfile import NamedTemporaryFile
from openai import OpenAI
import base64

# Setup OpenAI client (optional)
openai_api_key = st.secrets.get("OPENAI_API_KEY", None)
if openai_api_key:
    client = OpenAI(api_key=openai_api_key)

st.title("🗣️ AI Voice Bot")
user_input = st.text_input("Enter your message")

if st.button("Talk"):
    if user_input:
        # Use OpenAI if API key is set
        if openai_api_key:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response.choices[0].message.content
        else:
            # Simple fallback response
            reply = f"You said: {user_input}"

        st.markdown(f"**Bot:** {reply}")

        # Convert to speech
        tts = gTTS(reply)
        with NamedTemporaryFile(delete=True) as fp:
            tts.save(fp.name)
            audio_bytes = fp.read()
            st.audio(fp.name, format='audio/mp3')
    else:
        st.warning("Please enter a message.")
