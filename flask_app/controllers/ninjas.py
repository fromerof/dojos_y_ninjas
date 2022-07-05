from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#HOME

@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template("index.html",dojos=dojos)


@app.route("/create_dojo", methods=["POST"]) 
def create_dojo():
    Dojo.save(request.form)
    return redirect("/")

# NINJA

@app.route("/addNinja")
def addNinja():
    dojos = Dojo.get_all()
    return render_template("addNinja.html",dojos=dojos)

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect("/")

# SHOW DOJOS


@app.route("/showAll/<int:id>") #######
def showAll(id):
    data = {
        "id": id
    }
    return render_template("/dojoShow.html", dojos = Dojo.
    getDojo_withNinja(data))



