from flask import Blueprint, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
import pymysql

bp = Blueprint("brew", __name__, url_prefix='/posts')

from brew import mysql

# @bp.route("/")
# def home():
#     return render_template("pages/home.html")

# @bp.route("/about")
# def about():
#     return render_template("pages/about.html")


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        brew = request.form['brew']
        content = request.form['content']
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO railway.posts (author, title, content) VALUES (%s, %s, %s, %s)", (author, brew, title, content))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('posts.posts'))

    return render_template("posts/create.html")

@bp.route("/")
def posts():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM railway.posts")
    posts = cursor.fetchall()
    cursor.close()
    return render_template("posts/posts.html", posts=posts)