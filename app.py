from flask import Flask, render_template, request
import random

app = Flask(__name__)
def randomNews_genrator():
    subjects = [
        'nawaz sharif',
        'shahid afridi',
        'cats',
        'peshawar zalmi',
        'irfan',
        'zaland'
    ]
    actions = [
        'dances with',
        'cries for',
        'hits',
        'plays with',
        'takes a bath in',
        'eats'
    ]
    things_or_places = [
        'the floor',
        'the wall',
        'a buffalo',
        'the road',
        'monkeys',
        'the kitchen'
    ]
    random_subject = random.choice(subjects)
    random_action = random.choice(actions)
    random_thing = random.choice(things_or_places)
    headline = f"Breaking News: {random_subject} {random_action} {random_thing}!"
    return headline

def manuallyNews_genarator(subject, actions, places_or_things):
    headline = f"Breaking News: {subject} {actions} {places_or_things}"
    return headline
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    userinput = request.form.get("mode")

    if userinput == "1":
        headline = randomNews_genrator()
    elif userinput == "2":
        subject = request.form.get("subject")
        actions = request.form.get("actions")
        places_or_things = request.form.get("places_or_things")
        headline = manuallyNews_genarator(subject, actions, places_or_things)
    else:
        headline = "Invalid option."

    return render_template("result.html", headline=headline)

if __name__ == '__main__':
    app.run(debug=True)
