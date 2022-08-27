from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash
)


def response(message):
    flash(message)
    return render_template("index.html")

def create_random_url():
    import string
    import random
    string_out =[]
    upper = string.ascii_lowercase
    for i in range(1,random.randint(5,12)):
        string_out.append(upper[i])

    for i in range(1,random.randint(2,6)):
        random.shuffle(string_out)

    return "".join(string_out)