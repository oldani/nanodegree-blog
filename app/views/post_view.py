from flask import render_template, redirect, url_for, abort
from flask_classy import FlaskView, route
from flask_user import login_required, current_user
from ..models import PostModel
from ..forms import PostForm, CommentForm


class Post(FlaskView):
    """ Here will handle post creations, delete and update."""

    def get(self, entity_id):
        post = PostModel.get(entity_id)
        if not post:
            return redirect(url_for('Main:index'))
        comment_form = None
        if current_user.is_authenticated:
            comment_form = CommentForm()
        return render_template("post/post.html", post=post,
                               comment_form=comment_form)

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
        if int(entity_id) not in current_user.posts_list:
            abort(403)
        post = PostModel.get(entity_id)
        form = PostForm(obj=post)
        if form.validate_on_submit():
            form.populate_obj(post)
            post.update()
            return redirect(url_for("Post:get", entity_id=entity_id))
        return render_template("post/post_form.html", form=form,
                               url="Post:edit", entity_id=entity_id)

    @login_required
    @route("/delete/<entity_id>")
    def delete(self, entity_id):
        if int(entity_id) in current_user.posts_list:
            PostModel.delete(entity_id)
            return "Your post have been delete."
        return "You do not have a Post with an ID {}".format(entity_id)
