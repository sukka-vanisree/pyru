import streamlit as st
import requests

# App Title
st.title("🤖 Hugging Face Chat Assistant")

# Store chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("Enter your message:", "")

# Submit button
if st.button("Send"):
    if user_input.strip() != "":
        with st.spinner("Talking to assistant..."):
            # Hugging Face API endpoint and headers
            API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
            headers = {
                "Authorization": f"Bearer {st.secrets['hf_token']}"
            }
            payload = {"inputs": {"text": user_input}}

            response = requests.post(API_URL, headers=headers, json=payload)

            # If successful
            if response.status_code == 200:
                try:
                    generated_text = response.json()[0]["generated_text"]
                    # Store chat in history
                    st.session_state.chat_history.append(("You", user_input))
                    st.session_state.chat_history.append(("Assistant", generated_text))
                except Exception as e:
                    st.error("Error parsing response.")
            else:
                st.error("API Error. Please try again later.")

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Assistant:** {msg}")
