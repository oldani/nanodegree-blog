from flask import (
                    abort,
                    flash,
                    render_template,
                    redirect,
                    url_for
                  )
from flask_classy import FlaskView, route
from flask_user import login_required, current_user
from ..models import PostModel
from ..forms import PostForm, CommentForm


def user_own_post(post_id):
    """ Check if a user is the owner of a post. """
    if hasattr(current_user, 'posts_list'
               ) and int(post_id) in current_user.posts_list:
        return True
    return


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
        if user_own_post(entity_id):
            PostModel.delete(entity_id)
            flash("Your post have been delete.", "success")
        else:
            flash("You do not have a Post with an ID {}".format(
                  entity_id), "error")
        return redirect(url_for("Main:index"))

    @login_required
    def likes(self, entity_id):
        if user_own_post(entity_id):
            flash("You can't like your own post.", "error")

        post = PostModel.get(entity_id)
        if not post.has_liked(current_user.id):
            post.add_like(current_user.id)
        else:
            flash("You can only like a post once.", "error")

        return redirect(url_for("Post:get", entity_id=entity_id))
