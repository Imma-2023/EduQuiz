# utils.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from config import SCORE_LOG

def grade_quiz(questions, user_answers):
    """Grade quiz and return total score and per-question correctness"""
    score = 0
    results = []
    for q, ans in zip(questions, user_answers):
        if ans == q["answer"]:
            score += 1
            results.append(True)
        else:
            results.append(False)
    return score, results

def log_score(score):
    """Log quiz score to a CSV for dashboard"""
    os.makedirs(os.path.dirname(SCORE_LOG), exist_ok=True)
    if os.path.exists(SCORE_LOG):
        df = pd.read_csv(SCORE_LOG)
    else:
        df = pd.DataFrame(columns=["score"])
    df = pd.concat([df, pd.DataFrame({"score": [score]})], ignore_index=True)
    df.to_csv(SCORE_LOG, index=False)

def plot_dashboard():
    """Plot a bar chart of logged quiz scores"""
    if not os.path.exists(SCORE_LOG):
        return None
    df = pd.read_csv(SCORE_LOG)
    fig, ax = plt.subplots()
    ax.bar(range(1, len(df)+1), df["score"], color="skyblue")
    ax.set_xlabel("Attempt")
    ax.set_ylabel("Score")
    ax.set_title("Student Quiz Performance")
    return fig

def generate_hint(question, wrong_answer):
    """Provide simple AI-based hint for wrong answers"""
    return f"Think carefully about the question: '{question}'. You selected '{wrong_answer}'."
