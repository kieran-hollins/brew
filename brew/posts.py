from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from brew.database import get_db

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form['author'] or "Anonymous"
        title = request.form['title']
        image= request.files['brew']
        description = request.form['content']

        if image:
            #filename = secure_filename(brew.filename)
            image_blob = image.read()

            try:
                db = get_db()
                db.execute(
                    "INSERT INTO posts (author, title, brew, content) VALUES (?, ?, ?, ?)",
                    (author, title, image_blob, description),
                )
                db.commit()
            
            except Exception as e:
                print(f"Error: {e}")


            return redirect(url_for("posts.posts"))
        
    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    db = get_db()
    posts = db.execute(
        "SELECT author, title, brew, content, created FROM posts ORDER BY created DESC"
    ).fetchall()
    return render_template("posts/posts.html", posts=posts)