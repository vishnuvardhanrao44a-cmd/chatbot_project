import streamlit as st
from chatbot.bot import ChatBot

st.title("🤖 Vishnu's Chatbot")
st.write("A simple ML-based chatbot using scikit-learn")

bot = ChatBot()

user_input = st.text_input("You:", "")
if user_input:
    if user_input.lower() in ["quit", "exit"]:
        st.write("Bot: Goodbye Vishnu!")
    else:
        response = bot.get_response(user_input)
        st.write("Bot:", response)
