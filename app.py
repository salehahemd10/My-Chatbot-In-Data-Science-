import streamlit as st
import requests

st.set_page_config(page_title="Saleh's Chatbot")

st.markdown("""
    <h1 style='text-align: center;'>Saleh's AI Chatbot</h1>
    <p style='text-align: center;'>Ask me anything and I'll do my best to answer</p>
""", unsafe_allow_html=True)

API_URL = "http://127.0.0.1:8000/chat"

if "messages" not in st.session_state:
    st.session_state.messages = []  

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your question here...")

if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Preparing the reply..."):
            try:
                response = requests.post(API_URL, json={"user_input": user_input})
                if response.status_code == 200:
                    reply = response.json().get("response", "Sorry, I’m not sure how to help with that.")
                else:
                    reply = f"Connection error: {response.status_code}"
            except Exception as e:
                reply = f"Failed to connect to the server: {str(e)}"

        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
