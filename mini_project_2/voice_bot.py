import streamlit as st
from openai import OpenAI
from gtts import gTTS
import tempfile
import openai.error

# Initialize OpenAI client with API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Voice Bot 🎙️", layout="centered")
st.title("🤖 AI Voice Bot")
st.markdown("Type a message below and hear the AI respond.")

user_input = st.text_input("You:", "")

if st.button("Send") and user_input.strip() != "":
    with st.spinner("AI is thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content
            st.markdown("**AI:** " + reply)

            # Convert AI reply to speech using gTTS
            tts = gTTS(reply)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name, format="audio/mp3")

        except openai.error.RateLimitError:
            st.error("⚠️ You are sending requests too quickly. Please wait a moment and try again.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
