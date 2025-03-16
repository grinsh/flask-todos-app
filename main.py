from flask import Flask, render_template, url_for, request, redirect
from db import tasks
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", tasks=tasks)
    else:
        title = request.form['title']
        date_created = datetime.now()
        if tasks:
            new_id = tasks[-1]["id"] + 1
        else:
            new_id = 1
        new_task = {"id": new_id,
                    "title": title,
                    "date_created": date_created,
                    "completed": False}
        tasks.append(new_task)
        return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    for t in tasks:
        if(t["id"] == id):
            tasks.remove(t)
            break;
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    if(request.method=="GET"):
        for t in tasks:
            if(t["id"]==id):
                update_task = t
                break
        return render_template("update.html", task=update_task)
    else:
        title = request.form["title"]
        date_created = datetime.now()
        completed = request.form["completed"]

        for t in tasks:
            if t["id"]==id:
                t["title"] = title
                t["date_created"] = date_created
                t["completed"] = completed
        return redirect("/")

@app.get("/hello")
def hello():
   return "<h1>Hello world</h1>"

@app.get("/*")
def get_not_found():
    return render_template("notFound404.html")

# @app.get("/task/<int:id>")
# def get_task_by_id(id):
#     for t in tasks:
#         if t["id"] == id:
#             return t
#
#     return "Not Found 404"

if __name__ == "__main__":
    app.run(debug=True, use_evalex=False)