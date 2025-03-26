from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
db = SQLAlchemy(app)
# db class
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
        tasks_from_db =  Task.query.filter_by().all()
        return render_template("index.html", tasks=tasks_from_db)
    else:
        title = request.form['title']
        try:
            # assert title,  "Title must not be empty"
            new_task = Task(title=title)
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return render_template("errorMessage.html", message="Error with adding task...")

@app.route("/delete/<int:id>")
def delete(id):
    try:
        task_to_delete = Task.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return render_template("errorMessage.html", message= "An Error while deleting task...")


@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    if(request.method=="GET"):
        update_task = Task.query.get_or_404(id)
        return render_template("update.html", task=update_task)
    else:
        title = request.form["title"]
        date_created = datetime.now()
        completed = request.form["completed"] == "True"

        task_to_update = Task.query.get_or_404(id)
        task_to_update.title = title
        task_to_update.date_created = date_created
        task_to_update.completed = completed

        db.session.commit()
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