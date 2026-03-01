from flask import Flask, render_template, request, redirect, session, flash, abort
import secrets
import config
import db
import users
import items

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    all_items = items.get_items()
    return render_template("index.html", items=all_items)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        session["csrf_token"] = secrets.token_hex(16)
        return render_template("register.html", csrf_token=session["csrf_token"])

    if request.form.get("csrf_token") != session.get("csrf_token"):
        abort(403)

    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return redirect("/register")

    try:
        users.create_user(username, password1)
    except:
        flash("VIRHE: tunnus on jo varattu")
        return redirect("/register")

    flash("Käyttäjä luotu! Kirjaudu sisään.")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session["csrf_token"] = secrets.token_hex(16)
        return render_template("login.html", csrf_token=session["csrf_token"])

    if request.form.get("csrf_token") != session.get("csrf_token"):
        abort(403)

    username = request.form["username"]
    password = request.form["password"]

    user_id = users.check_login(username, password)
    if user_id:
        session["user_id"] = user_id
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")
    else:
        flash("VIRHE: väärä tunnus tai salasana")
        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/new_item", methods=["GET", "POST"])
def new_item():
    if "user_id" not in session:
        flash("Kirjaudu sisään lisätäksesi kirjan")
        return redirect("/login")

    if request.method == "GET":
       
        categories = items.get_categories()
        return render_template("new_item.html", categories=categories, selected_categories=[])

    
    if request.form["csrf_token"] != session.get("csrf_token"):
        abort(403)

    title = request.form["title"]
    author = request.form["author"]
    review = request.form["review"]
    user_id = session["user_id"]
    selected_categories = request.form.getlist("categories") 

    
    items.add_item(title, author, review, user_id)

    item_id = db.last_insert_id()

    items.add_item_categories(item_id, selected_categories)

    flash("Kirja lisätty onnistuneesti!")
    return redirect("/")


@app.route("/edit_item/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = items.get_item(item_id)
    if not item:
        flash("Arviointia ei löytynyt")
        return redirect("/")

    if session.get("user_id") != item["user_id"]:
        flash("Et voi muokata tätä arviota")
        return redirect("/")

    if request.method == "GET":
        categories = items.get_categories()
        selected_categories = []
        return render_template("edit_item.html",
                               item=item,
                               categories=categories,
                               selected_categories=selected_categories)
   
    if request.form["csrf_token"] != session.get("csrf_token"):
        abort(403)

    title = request.form["title"]
    author = request.form["author"]
    review = request.form["review"]
    selected_categories = request.form.getlist("categories")

    items.update_item(item_id, title, author, review)
    items.update_item_categories(item_id, selected_categories)
    flash("Arviointi päivitetty!")
    return redirect("/")


@app.route("/remove_item/<int:item_id>", methods=["POST"])
def remove_item(item_id):
    if request.form["csrf_token"] != session.get("csrf_token"):
        abort(403)

    item = items.get_item(item_id)
    if not item or session.get("user_id") != item["user_id"]:
        flash("Et voi poistaa tätä arviota")
        return redirect("/")

    items.delete_item(item_id)
    flash("Arviointi poistettu!")
    return redirect("/")


@app.route("/search")
def search():
    query = request.args.get("query", "")
    results = items.search_items(query)
    return render_template("search.html", query=query, results=results)


@app.route("/user/<int:user_id>")
def user_page(user_id):
    user = users.get_user(user_id)
    user_items = items.get_items_by_user(user_id)
    item_count = items.count_items_by_user(user_id)

    return render_template("user.html",
                           user=user,
                           items=user_items,
                           item_count=item_count)


@app.route("/comment_item/<int:item_id>", methods=["POST"])
def comment_item(item_id):
    if "user_id" not in session:
        flash("Kirjaudu sisään kommentoidaksesi")
        return redirect("/login")
    if request.form["csrf_token"] != session.get("csrf_token"):
        abort(403)

    text = request.form["comment"]
    items.add_comment(item_id, session["user_id"], text)
    flash("Kommentti lisätty!")
    return redirect("/")
