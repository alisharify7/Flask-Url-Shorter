from flask import (
    render_template,
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
    for i in range(1,random.randint(4,8)):
        string_out.append(upper[i])

    for i in range(1,random.randint(2,6)):
        random.shuffle(string_out)

    return "".join(string_out)
