from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def student_form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subjects = request.form.getlist("subjects")
        return render_template("submitted.html", name=name, email=email, subjects=subjects)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
