import streamlit as st
import webbrowser

# ----------------- Page Setup -----------------
st.set_page_config(page_title="Farmer Crop Doctor App", page_icon="🌾")
st.title("🌾 Farmer Crop Doctor – Disease & Yield Support")

# ----------------- Language Selection -----------------
language = st.selectbox("Choose Language / భాషను ఎంచుకోండి / भाषा चुनें:", ["English", "Telugu", "Hindi"])

# ----------------- Translations -----------------
translations = {
    "English": {
        "crop_label": "Select your crop:",
        "symptom_label": "Describe the symptoms or yield issue:",
        "button": "Get Suggestion",
        "warning": "Please select a crop and enter symptoms.",
        "advice": "🩺 Suggested Advice",
        "footer": "Note: These are general suggestions. Consult a local agriculture expert for precise help.",
        "chat_prompt": "Need more help? Use the full chatbot here:",
        "chat_button": "Go to Full Chatbot"
    },
    "Telugu": {
        "crop_label": "మీ పంటను ఎంచుకోండి:",
        "symptom_label": "లక్షణాలు లేదా దిగుబడి సమస్యను వివరించండి:",
        "button": "సూచనలను పొందండి",
        "warning": "దయచేసి పంటను ఎంచుకొని లక్షణాలను నమోదు చేయండి.",
        "advice": "🩺 సిఫార్సు చేసిన సూచనలు",
        "footer": "గమనిక: ఇవి సాధారణ సూచనలు. ఖచ్చితమైన సహాయం కోసం స్థానిక వ్యవసాయ నిపుణుడిని సంప్రదించండి.",
        "chat_prompt": "మరింత సహాయం కావాలా? పూర్తి చాట్‌బాట్‌ను ఉపయోగించండి:",
        "chat_button": "పూర్తి చాట్‌బాట్‌కు వెళ్లండి"
    },
    "Hindi": {
        "crop_label": "अपनी फसल चुनें:",
        "symptom_label": "लक्षण या पैदावार की समस्या बताएं:",
        "button": "सुझाव प्राप्त करें",
        "warning": "कृपया फसल चुनें और लक्षण दर्ज करें।",
        "advice": "🩺 सुझाई गई सलाह",
        "footer": "नोट: ये सामान्य सुझाव हैं। सटीक सहायता के लिए कृषि अधिकारी से संपर्क करें।",
        "chat_prompt": "और मदद चाहिए? पूरा चैटबॉट यहाँ देखें:",
        "chat_button": "पूरा चैटबॉट खोलें"
    }
}

# ----------------- Crop Advice -----------------
crop = st.selectbox(
    translations[language]["crop_label"],
    ["Select", "Rice", "Wheat", "Maize", "Cotton", "Tomato", "Groundnut", "Chili", "Sugarcane"]
)

symptoms = st.text_area(translations[language]["symptom_label"])

if st.button(translations[language]["button"]):
    if crop == "Select" or not symptoms:
        st.warning(translations[language]["warning"])
    else:
        st.subheader(translations[language]["advice"])
        symptom_text = symptoms.lower()

        # Smart suggestions
        if "yellow" in symptom_text:
            st.write(f"{crop}: Yellow leaves? Possibly nitrogen deficiency. Apply compost or nitrogen fertilizer.")
        elif "spots" in symptom_text:
            st.write(f"{crop}: Spots on leaves may be from fungus. Use proper fungicide spray.")
        elif "wilt" in symptom_text:
            st.write(f"{crop}: Wilting may mean poor soil drainage or root disease.")
        elif "insect" in symptom_text or "pest" in symptom_text:
            st.write(f"{crop}: Pests? Use neem oil or herbal repellents to control.")
        elif "low yield" in symptom_text or "less production" in symptom_text:
            st.write(f"{crop}: Low yield may result from weak soil or seeds. Rotate crops, enrich soil, and water properly.")
        else:
            st.write(f"{crop}: Follow healthy irrigation, use balanced fertilizers, and monitor leaf changes.")

        st.info(translations[language]["footer"])

# ----------------- Chatbot Redirect Button -----------------
st.markdown("---")
st.subheader("🤖 AgriBot – Smart Chat Assistant")

st.write(translations[language]["chat_prompt"])

# Add the Hugging Face chatbot link here
huggingface_chatbot_url = "https://huggingface.co/chat/assistant/684d57647d87375a3fc54dcc"

# Open in new tab using HTML and JS
chat_button_html = f"""
    <a href="{huggingface_chatbot_url}" target="_blank">
        <button style='background-color:#4CAF50; color:white; padding:10px 24px; border:none; border-radius:8px; font-size:16px;'>
            {translations[language]["chat_button"]}
        </button>
    </a>
"""
st.markdown(chat_button_html, unsafe_allow_html=True)
