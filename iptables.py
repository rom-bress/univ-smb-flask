# save this as app.py
from flask import Flask
from flask import render_template, redirect
from flask import session, request
app = Flask(__name__)
app.secret_key ="abcdef"
   


@app.route("/")
def start():
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/formulaire")
    return render_template("index.html")

@app.route("/rules_filter")
def rules_filter():
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/formulaire")
    return render_template("filter.html")

@app.route("/rules_nat")
def rules_nat():
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/formulaire")
    return render_template("nat.html")

@app.route("/rules_add_nat")
def rules_nat_add():
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/formulaire")
    return render_template("ajout_nat.html")

@app.route("/alias")
def alias():
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/formulaire")
    return render_template("alias.html")

@app.route("/formulaire", methods=["POST", "GET"])
def formulaire():
    if request.method == "POST":
        # record the user name
        session["name"] = request.form.get("username")
        # redirect to the main page
        return redirect("/")
    else :
        return render_template("formulaire.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect ( url_for('index'))
