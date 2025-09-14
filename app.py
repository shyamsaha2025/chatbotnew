# 🤖 AI Chatbot Frontend - Part 1: Simple Chat UI
#
# NOTE FOR ENTIRE EXERCISE:
# This frontend file (app.py) will NOT change throughout the 7-part tutorial.
# You will only work on different backend.py logic files for each part.
# When your initial backend.py is ready, uncomment lines 15-16 below to connect to your AI backend.

import streamlit as st
from backend import get_ai_response

print("🚀 Starting chatbot...")

# Configure the web page appearance
st.set_page_config(page_title="My First GPT Chat App", page_icon="🤖")
st.title("🤖 My First GPT Chat App")

# Create text input area for user messages
user_message = st.text_area("Your message:", height=100)

# Handle send button click
if st.button("📤 Send") and user_message:
    # UNCOMMENT THESE TWO LINES WHEN YOUR BACKEND.PY IS READY:
   
    with st.spinner("Connecting to OpenAI..."):
        response = get_ai_response(user_message)
    

    # Display the conversation
    st.markdown("**You:**")
    st.write(user_message)

    
    st.markdown("**AI:**")
    st.write(response)
