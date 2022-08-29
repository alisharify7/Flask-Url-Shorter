import config 
import os
from helpers import helpers
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    flash
)

app = Flask(__name__)
app.config.from_object(config.Production)

#  -----------DB Model------------
import  datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    link = db.Column(db.String(128))
    date = db.Column(db.DateTime,default=datetime.datetime.now()) 

class Link(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key=True)
    id_users = db.Column(db.Integer())
    link_short = db.Column(db.String(128))

if config.db_name not in os.listdir():
    db.create_all()
# ------------End DB Model----------


@app.route("/",methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        username = request.form.get("username",None)
        link = request.form.get("link",None)

        if not username:
            flash("Username Is Empty")
            return render_template("index.html")
        if not link:
            flash("link Is Empty")
            return render_template("index.html")

        # check db for duplicate user and link
        db_user_ans =User.query.filter(User.username==username and User.link == username).first()
        if db_user_ans:
            return helpers.response("This User Name and Link is Exists Create with New Username")

        # add User to db
        new_User = User(username=username,link=link)
        db.session.add(new_User)
        db.session.commit()

        # create url for link 
        url =  helpers.create_random_url()
        # add to db link and short link 
        new_link = Link(id_users = new_User.id, link_short=url)
        db.session.add(new_link)
        db.session.commit()

        flash(f"Link Created Successfully, {config.host}/L/{url}")
        return render_template("index.html")


@app.route('/L/<url>')
def search(url):
    if not url:
        return jsonify("Error 83")

    #  query to link to find link
    new_link = Link.query.filter(Link.link_short == url).first()
    if not new_link:
        return jsonify("Invalid Link :(")

    new_user = User.query.filter(User.id == new_link.id_users).first()
    return redirect(f"http://{new_user.link}")
   

if __name__ == "__main__":
    app.run(debug=True)
