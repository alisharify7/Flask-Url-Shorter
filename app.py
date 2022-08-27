from flask import (
    Flask,
    redirect,
    render_template,
    flash
    )
from config import Development

app = Flask(__name__)
app.config.from_object(Development)


@app.route("/")
def index():
    return render_template("index.html")