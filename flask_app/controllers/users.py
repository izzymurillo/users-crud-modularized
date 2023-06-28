from flask_app import app

from flask import render_template, request, redirect

from flask_app.models.user_model import User

# HOME PAGE 
@app.route("/")
def index():
    return render_template("create.html")

# ------------  CREATE - RENDERS THE FORM  ------------
@app.route("/users/new")
def new_user_page():
    return render_template("create.html")

# -------  CREATE - POST ROUTE - SENDS IN INFORMATION  -------
@app.route("/users/create", methods = ["POST"])
def create_user():
    print(request.form)
    user_id = User.create(request.form)
    return redirect("/show/"+ f"{user_id}")

# ------------ READ ALL - SHOW ALL USERS   ------------
@app.route("/users")
def show_all():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

# ------------   READ ONE - SHOW ONE USER   ------------
@app.route("/show/<int:id>")
def show_one(id):
    data = {'id' : id}
    one_user = User.get_one(id)
    print(one_user)
    return render_template("read_one.html", one_user=User.get_one(data))

# ------------   UPDATE - RENDERS THE FORM   ------------
@app.route("/user/edit/<int:id>")
def edit(id):
    data = {"id":id}
    return render_template("edit_user.html",user=User.get_one(data))

# ------------   UPDATE - POST ROUTE   ------------
@app.route("/user/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")

# ------------   DELETE   ------------
@app.route("/user/delete/<int:id>")
def delete(id):
    data = {"id":id}
    User.delete(data)
    return redirect("/users")