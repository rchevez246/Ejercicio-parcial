from db import insertNewPerson
from Person import Person
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

# route para insert

@app.route("/insertemail", methods=["GET", "POST"])
def new_email():
    if request.method == "GET":
        return render_template("home.html")
    
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        person = Person(name, email)
        insertNewPerson(person)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)