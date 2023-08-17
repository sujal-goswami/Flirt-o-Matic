from flask import Flask, render_template, request
from requests import get

app2 = Flask(__name__)

def generate_pickup_line(user_input):
    pickup_line = get("https://vinuxd.vercel.app/api/pickup").json()["pickup"]
    return pickup_line


@app2.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        pickup_line = generate_pickup_line(user_input)
        return render_template("index.html", pickup_line=pickup_line)

    return render_template("index.html")

if __name__ == "__main__":
    app2.run(debug=True)