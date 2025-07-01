import streamlit as st

# Title
st.set_page_config(page_title="Farmer Crop Doctor App", page_icon="🌾")
st.title("🌾 Farmer Crop Doctor – Disease & Yield Support")

# Language Selection
language = st.selectbox("Choose Language / భాషను ఎంచుకోండి / भाषा चुनें:", ["English", "Telugu", "Hindi"])

# Translation dictionary (basic)
translations = {
    "English": {
        "crop_label": "Select your crop:",
        "symptom_label": "Describe the symptoms or yield issue:",
        "button": "Get Suggestion",
        "warning": "Please select a crop and enter symptoms.",
        "advice": "🩺 Suggested Advice",
        "footer": "Note: These are general suggestions. Consult a local agriculture expert for precise help.",
    },
    "Telugu": {
        "crop_label": "మీ పంటను ఎంచుకోండి:",
        "symptom_label": "లక్షణాలు లేదా దిగుబడి సమస్యను వివరించండి:",
        "button": "సూచనలను పొందండి",
        "warning": "దయచేసి పంటను ఎంచుకొని లక్షణాలను నమోదు చేయండి.",
        "advice": "🩺 సిఫార్సు చేసిన సూచనలు",
        "footer": "గమనిక: ఇవి సాధారణ సూచనలు. ఖచ్చితమైన సహాయం కోసం స్థానిక వ్యవసాయ నిపుణుడిని సంప్రదించండి.",
    },
    "Hindi": {
        "crop_label": "अपनी फसल चुनें:",
        "symptom_label": "लक्षण या पैदावार की समस्या बताएं:",
        "button": "सुझाव प्राप्त करें",
        "warning": "कृपया फसल चुनें और लक्षण दर्ज करें।",
        "advice": "🩺 सुझाई गई सलाह",
        "footer": "नोट: ये सामान्य सुझाव हैं। सटीक सहायता के लिए कृषि अधिकारी से संपर्क करें।",
    }
}

# Crop selection
crop = st.selectbox(
    translations[language]["crop_label"],
    ["Select", "Rice", "Wheat", "Maize", "Cotton", "Tomato", "Groundnut", "Chili", "Sugarcane"]
)

# Symptom input
symptoms = st.text_area(translations[language]["symptom_label"])

# Submit
if st.button(translations[language]["button"]):
    if crop == "Select" or not symptoms:
        st.warning(translations[language]["warning"])
    else:
        st.subheader(translations[language]["advice"])

        symptom_text = symptoms.lower()

        # Optimistic, friendly suggestions
        if "yellow" in symptom_text:
            st.write(f"{crop}: Leaves turning yellow? It might be nutrient deficiency. Try adding organic compost or nitrogen-based fertilizer.")
        elif "spots" in symptom_text:
            st.write(f"{crop}: Leaf spots are often caused by fungal or bacterial infection. Use a mild fungicide and avoid overhead watering.")
        elif "wilt" in symptom_text:
            st.write(f"{crop}: Wilting may be due to overwatering or root rot. Improve drainage and check roots.")
        elif "insect" in symptom_text or "pest" in symptom_text:
            st.write(f"{crop}: Pest attack? Use neem oil spray or try natural pest repellents like garlic or chili extract.")
        elif "low yield" in symptom_text or "less production" in symptom_text:
            st.write(f"{crop}: Low yield can happen due to poor soil, seed quality, or climate. Use certified seeds and consider crop rotation.")
        else:
            st.write(f"{crop}: General advice – Maintain regular irrigation, avoid overuse of chemicals, and consult nearby agri center.")

        st.info(translations[language]["footer"])
