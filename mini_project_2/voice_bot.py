import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import openai
import numpy as np
import wave
import av
import os
from gtts import gTTS
import tempfile
import time

# Set your OpenAI API key
openai.api_key = st.secrets["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"]  # use Streamlit secrets for safety

# Title
st.title("🎙️ AI Voice Bot using OpenAI + Streamlit")

# Save audio as WAV
def save_audio_to_file(frames, sample_rate=16000, filename="audio.wav"):
    wf = wave.open(filename, "wb")
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()
    return filename

# Transcribe using OpenAI Whisper
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]

# Chat with GPT
def chat_with_gpt(prompt):
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful AI voice assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content

# Speak using gTTS
def speak_text(text):
    tts = gTTS(text=text, lang="en")
    tmp_fp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_fp.name)
    return tmp_fp.name

# Audio processor class for streamlit-webrtc
class AudioProcessor(AudioProcessorBase):
    def __init__(self) -> None:
        self.frames = []

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray()
        self.frames.append(frame.planes[0].to_bytes())
        return frame

    def get_audio_data(self):
        return self.frames

# WebRTC Stream
ctx = webrtc_streamer(
    key="send-audio",
    mode="sendonly",
    audio_receiver_size=1024,
    audio_frame_callback=None,
    media_stream_constraints={"audio": True, "video": False},
    async_processing=True
)

# Start button to process
if ctx.audio_receiver:
    if st.button("🎤 Transcribe and Chat"):
        audio_processor = ctx.audio_processor
        if audio_processor:
            with st.spinner("Processing audio..."):
                audio_data = audio_processor.get_audio_data()
                audio_file_path = save_audio_to_file(audio_data)

                # Transcribe
                transcript = transcribe_audio(audio_file_path)
                st.success(f"📝 You said: {transcript}")

                # Chat response
                reply = chat_with_gpt(transcript)
                st.info(f"🤖 Bot says: {reply}")

                # TTS
                speech_fp = speak_text(reply)
                audio_bytes = open(speech_fp, "rb").read()
                st.audio(audio_bytes, format="audio/mp3")
