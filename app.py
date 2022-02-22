from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route("/insertemail", methods=["GET", "POST"])
def new_email():
    if request.method == "GET":
        return render_template("home.html")
    
    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        salary = request.form.get("salary")
        person = Person(name, age, salary)
        insertNewPerson(person)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)