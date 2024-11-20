from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answers = {
            "q1": request.form.get("q1"),
            "q2": request.form.get("q2"),
            "q3": request.form.get("q3"),
            "q4": request.form.get("q4"),
            "q5": request.form.get("q5"),
        }
        # Analyze personality based on answers
        analysis = analyze_personality(answers)
        return render_template("result.html", analysis=analysis)
    return render_template("index.html")

def analyze_personality(answers):
    traits = []
    if answers["q1"] == "Yes":
        traits.append("You are adventurous.")
    if answers["q2"] == "Yes":
        traits.append("You are empathetic.")
    if answers["q3"] == "No":
        traits.append("You prefer stability.")
    if answers["q4"] == "Yes":
        traits.append("You are creative.")
    if answers["q5"] == "No":
        traits.append("You value logic over emotions.")
    return traits if traits else ["Your personality is unique and can't be easily categorized!"]

if __name__ == "__main__":
    app.run(debug=True)
