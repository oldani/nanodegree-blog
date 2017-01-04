from flask import render_template, request, redirect, url_for
from flask_classy import FlaskView, route
from ..models import PostModel


class Post(FlaskView):
    """Here will handle post creations, delete and update."""

    def get(self, id):
        post = PostModel()
        post = post.get(id)
        return render_template("post.html", post=post)

    @route("/new/", methods=["GET", "POST"])
    def new(self):
        if request.method == "POST":
            post = request.form.to_dict(flat=True)
            post = PostModel(**post)
            post.put()
            return redirect(url_for("Post:get", id=post.id))
        return render_template("new_post.html")

    def edit(self, id):
        post = PostModel()
        post = post.get(id)
        return render_template("new_post.html", post=post)
