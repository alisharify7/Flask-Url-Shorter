import config 
import os
from helpers import helpers
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash
)

app = Flask(__name__)
app.config.from_object(config.Development)

#  -----------DB Model------------
import  datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    link = db.Column(db.String(128))
    date = db.Column(db.DateTime,default=datetime.datetime.now()) 


if config.db_name not in os.listdir():
    db.create_all()
# ------------End DB Model----------



@app.route("/",methods=["GET", "POST"])
def index():
    username = request.form.get("username",None)
    link = request.form.get("link",None)
    if not username:
        flash("Username Is Empty")
        return render_template("index.html")
    if not link:
        flash("link Is Empty")
        return render_template("index.html")
    
    # check db for duplicate user and link
    db_user_ans =User.query.filter_by(User.username==username and User.link == username)
    if not db_user_ans:
        helpers.response("This User Name and Link is Exists Create with New Username")

    # add User to db
    new_User = User(username=username,link=link)
    db.session.add(new_User)
    db.session.commit()















    

if __name__ == "__main__":
    app.run('0.0.0.0',port=8080,debug=True)