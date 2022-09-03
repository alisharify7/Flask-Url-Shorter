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



def url_remover(url):
    """
    This Function remove all not important Part From Url
    """
    www = True    
    https = True    
    while(www):
        if "www" in url:
            url = url.replace("www","")
            url = url.strip()
            wwww = False
    while(https):
        if "https" in url:
            url = url.replace("https","")
            url = url.strip()
            https= False
        if "http" in url:
            url = url.replace("http","")
            url = url.strip()
            https= False


def validate_url(url):
    # TODO 
    # [x] check and validate 55
    # [0] handel real address
    # [0] clean input string
    return url_remover(url)

        