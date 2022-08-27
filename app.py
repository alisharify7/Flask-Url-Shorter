from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash
    )
from config import Development

app = Flask(__name__)
app.config.from_object(Development)


@app.route("/",methods=["GET", "POST"])
def index():
    print(request.form)
    flash("hello From Server","error")
    return render_template("index.html")


if __name__ == "__main__":
    app.run('0.0.0.0',port=8080,debug=True)