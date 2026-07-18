import streamlit as st
from chatbot import get_response

st.title("Customer Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Type your message")

if st.button("Send"):
    if user_input:
        bot_reply = get_response(user_input)
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Bot", bot_reply))

for sender, message in st.session_state.messages:
    st.write(f"**{sender}:** {message}")