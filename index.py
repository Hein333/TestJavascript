from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  username = "Alice"
  user_score = 95
  return render_template(
      "index.html", name=username, score=user_score
  )  # Renders template.html
