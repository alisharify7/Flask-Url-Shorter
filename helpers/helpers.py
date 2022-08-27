from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash
)

from ..app import app


def response(message):
    flash(message)
    return render_template("index.html")