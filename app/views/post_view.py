from flask import render_template, redirect, url_for
from flask_classy import FlaskView, route
from flask_user import login_required, current_user
from ..models import PostModel
from ..forms import PostForm


class Post(FlaskView):
    """ Here will handle post creations, delete and update."""

    def get(self, entity_id):
        post = PostModel()
        post = post.get(entity_id)
        return render_template("post/post.html", post=post)

    @login_required
    @route("/new/", methods=["GET", "POST"])
    def new(self):
        form = PostForm()
        if form.validate_on_submit():
            post = PostModel(user=current_user.username, **form.data)
            post.put()
            current_user.add_post(post.id)
            return redirect(url_for("Post:get", entity_id=post.id))
        return render_template("post/post_form.html", form=form,
                               url="Post:new")

    @login_required
    @route("/edit/<entity_id>", methods=["GET", "POST"])
    def edit(self, entity_id):
        post = PostModel()
        entity = post.get(entity_id)
        form = PostForm(**entity)
        if form.validate_on_submit():
            post.update(entity_id, form.data)
            return redirect(url_for("Post:get", entity_id=entity_id))
        return render_template("post/post_form.html", form=form,
                               url="Post:edit", entity_id=entity_id)
