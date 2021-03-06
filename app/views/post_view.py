from flask import (
                    abort,
                    flash,
                    render_template,
                    redirect,
                    url_for
                  )
from flask_classy import FlaskView, route
from flask_user import login_required, current_user
from ..forms import PostForm, CommentForm
from ..models import PostModel
from ..helpers import user_own_post


class Post(FlaskView):

    def get(self, entity_id):
        """ Retrieve a post, if not exits redirect to home,
            and if authenticated render a comment form. """
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
        """ Handle editing a post, if the user is not the owner,
            throw a 403 error. """
        post = PostModel.get(entity_id)
        if post and not user_own_post(entity_id):
            abort(403)
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
        if PostModel.delete(entity_id):
            flash("Your post have been delete.", "success")
        else:
            flash("You do not have a Post with an ID {}".format(
                  entity_id), "error")
        return redirect(url_for("Main:index"))

    @login_required
    def likes(self, entity_id):
        post = PostModel.get(entity_id)
        if post and not user_own_post(entity_id):
            if not post.has_liked(current_user.id):
                post.add_like(current_user.id)
            else:
                flash("You can only like a post once.", "error")
        else:
            flash("You can't like your own post.", "error")
        return redirect(url_for("Post:get", entity_id=entity_id))
