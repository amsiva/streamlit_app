import streamlit as st
from dotenv import load_dotenv
import requests


st.header("Chatbot APP using Groq")


if "message" not in st.session_state:
    st.session_state.message = []

for msg in st.session_state.message:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt:= st.chat_input("You:"):
    st.session_state.message.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("AI"):
        with st.spinner("Thinking..."):
            response = requests.post("http://localhost:8000/generate", json={"message": prompt})
            result = response.json()['message']
            st.markdown(result)
            st.session_state.message.append({"role": "AI", "content": result})
        