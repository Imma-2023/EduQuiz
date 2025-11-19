# app.py
import streamlit as st
from quiz_data import quiz_questions
from utils import grade_quiz, log_score, plot_dashboard, generate_hint
from config import PREMIUM_FEATURES_ENABLED, DONATION_LINK

# Page config
st.set_page_config(page_title="EduQuiz", layout="wide")
st.title("🎓 EduQuiz: Interactive Learning for Students")
st.write("Test your knowledge, get instant feedback, and track your progress!")

# Sidebar: Monetization
st.sidebar.header("Support EduQuiz")
st.sidebar.info("Donate or unlock premium quizzes!")
if st.sidebar.button("Donate"):
    st.sidebar.success(f"Thank you! Visit {DONATION_LINK}")
premium_toggle = st.sidebar.checkbox("Unlock Premium Features") if PREMIUM_FEATURES_ENABLED else False

# Quiz
st.header("Quiz Time! Answer the questions below:")
user_answers = []
for idx, q in enumerate(quiz_questions):
    st.subheader(f"Q{idx+1}: {q['question']}")
    choice = st.radio("Select an answer:", q["options"], key=f"q{idx}")
    user_answers.append(choice)

# Submit
if st.button("Submit Answers"):
    score, results = grade_quiz(quiz_questions, user_answers)
    log_score(score)

    st.subheader("Results:")
    for idx, correct in enumerate(results):
        if correct:
            st.success(f"Q{idx+1}: Correct!")
        else:
            st.error(f"Q{idx+1}: Incorrect. Hint: {generate_hint(quiz_questions[idx]['question'], user_answers[idx])}")

    st.info(f"Your Total Score: {score}/{len(quiz_questions)}")

# Dashboard
st.header("📊 Your Quiz Progress")
if st.button("Show Performance Dashboard"):
    fig = plot_dashboard()
    if fig:
        st.pyplot(fig)
    else:
        st.info("No quiz attempts yet. Submit answers to see the dashboard.")
