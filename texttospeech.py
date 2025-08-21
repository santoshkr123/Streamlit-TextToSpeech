import streamlit as st
from gtts import gTTS

def text_to_speech(text,accent="en"):
    tts=gTTS(text=text,lang=accent)
    tts.save("output.mp3")
    return "output.mp3"


st.title("Text-to-Speech Converter")
st.markdown("Convert your text into audio")

text_input=st.text_area("Enter your text for conversion :","Hello this is a text to speech demo")
accent=st.selectbox("Select your Accent:",["en","hi","fr","de"])


if st.button("Convert your text"):
    if text_input.strip():
        audio_file=text_to_speech(text_input,accent)
        st.audio(audio_file,format="audio/mp3")
        with open(audio_file,"rb")as file :
            st.download_button(label="Download audio",data=file,file_name="speech.mp3",mime="audio/mp3")
    

