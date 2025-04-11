import streamlit as st
import google.generativeai as genai

# Page layout
st.header('subGPT')
st.title("🤖 Gemini Chatbot")

# Configure Gemini API
genai.configure(api_key="API_KEY")  # Replace with your real API key

# Use the best Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro-002")

# Initialize chat session using Streamlit session_state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user
user_input = st.chat_input("Enter your prompt...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Check for exit
    if user_input.lower() in ['exit', 'quit']:
        st.write("Goodbye!")
    else:
        # Send message to Gemini
        response = st.session_state.chat.send_message(user_input)

        # Show response
        with st.chat_message("assistant"):
            st.markdown(response.text)

        # Save assistant response
        st.session_state.messages.append({"role": "assistant", "content": response.text})
