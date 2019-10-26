from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/wellness-weekly')
def wellness_weekly():
    return render_template("wellness-weekly.html")

@app.route('/wellness-choice')
def wellness_choice():
    return render_template("wellness-choice.html")

@app.route('/journal')
def journal():
    entries = [
        { "text": "testing testing testing", "date": "2019-10-26", "day_of_week": "Saturday" }
    ]
    return render_template("journal.html", entries=entries)

@app.route('/wellness')
def wellness():
    words = ["happy", "sad", "scared", "tired", "angry", "excited", "content",\
                "unsafe", "blessed", "suicidal", "hopeless", "hopeful", \
                "purposeful", "confused", "frustrated", "annoyed", "tempermental",\
                "heavy", "overwhelmed", "conflicted", "guilty", "ashamed", \
                "embarressed", "needy", "lonely", "weak", "strong", "elevated", \
                "joyful", "thankful", "peaceful", "rejevunated", "accomplised", \
                "clean", "dirty", "misunderstood", "understood"]
    return render_template("wellness.html", words=words)
