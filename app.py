from flask import Flask, render_template, request
from models import Question
from datetime import datetime
import random

app = Flask(__name__)


questions = [
    Question("Capital of Nigeria?", ["A. Abuja", "B. Lagos", "C. Kano", "D. Ibadan"], "A. Abuja"),
    Question("2 + 2 = ?", ["A. 3", "B. 4", "C. 5", "D. 6"], "B. 4"),
    Question("Largest planet?", ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "C. Jupiter"),
    Question("HTML stands for?", [
        "A. Hyper Text Markup Language",
        "B. High Text Machine Language",
        "C. Home Tool Markup Language",
        "D. Hyperlinks Text Mark"
    ], "A. Hyper Text Markup Language"),
    Question("Which is a browser?", ["A. Chrome", "B. Python", "C. Linux", "D. Windows"], "A. Chrome"),
    Question("5 x 6 = ?", ["A. 30", "B. 25", "C. 20", "D. 35"], "A. 30"),
    Question("Water freezes at?", ["A. 0°C", "B. 10°C", "C. 50°C", "D. 100°C"], "A. 0°C"),
    Question("Which is a programming language?", ["A. HTML", "B. CSS", "C. Python", "D. HTTP"], "C. Python"),
    Question("Which organ pumps blood?", ["A. Brain", "B. Liver", "C. Heart", "D. Kidney"], "C. Heart"),
    Question("Sun rises in the?", ["A. West", "B. North", "C. South", "D. East"], "D. East"),
    Question("Color of the sky?", "Blue"),
]

@app.route("/")
def home():
    random.shuffle(questions)
    return render_template("index.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    score = 0
    results = []

    for i, question in enumerate(questions):
        user_answer = request.form.get(f"q{i}")

        if question.is_correct(user_answer):
            score += 1

        results.append({
            "question": question.text,
            "your_answer": user_answer,
            "correct_answer": question.answer
        })

    time_submitted = datetime.now()

    return render_template(
        "result.html",
        score=score,
        total=len(questions),
        time=time_submitted,
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)