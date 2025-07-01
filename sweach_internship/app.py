import streamlit as st
import datetime

st.title("🧠 Quiz Application")
st.subheader("Welcome to the Quiz Challenge!")

# Step 1: Get user's name
name = st.text_input("Enter your name to start:")

# Quiz questions
questions = {
    "What is the capital of India?": "New Delhi",
    "Which language is used to build Android apps?": "Java",
    "What is 9 * 9?": "81"
}

# Step 2: Conduct quiz
if name:
    st.markdown(f"### Hello, {name}! Let's begin the quiz 🎯")
    score = 0
    responses = {}

    for i, (question, answer) in enumerate(questions.items()):
        user_answer = st.text_input(f"Q{i+1}: {question}")
        responses[question] = user_answer.strip()

    if st.button("Submit Quiz"):
        for q, a in questions.items():
            if responses[q].lower() == a.lower():
                score += 1

        total = len(questions)
        st.write(f"Your Score: **{score}/{total}**")

        # Step 3: Generate certificate if passed
        if score >= total * 0.7:
            st.success("🎉 Congratulations! You passed the quiz.")
            st.markdown("---")
            st.markdown("## 🟣 Certificate of Achievement 🟣")
            st.markdown(f"**Name:** {name}  \n**Score:** {score}/{total}  \n**Date:** {datetime.date.today()}")
            st.markdown("Well done on successfully completing the quiz!")
        else:
            st.error("❌ You did not pass. Try again!")
