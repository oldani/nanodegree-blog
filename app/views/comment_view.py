from flask import jsonify
from flask_classy import FlaskView
from flask_user import current_user, login_required
from ..models import CommentModel, PostModel
from ..forms import CommentForm


class Comment(FlaskView):

    def get(self):
        pass

    def all(self, post_id):
        comment = CommentModel()
        comment.query.add_filter('post_id', '=', int(post_id))
        return jsonify(comment.fetch())

    @login_required
    def post(self, post_id):
        form = CommentForm()
        if form.validate_on_submit():
            post = PostModel().get(post_id)
            post = PostModel(**post)
            comment = CommentModel(user=current_user.username, **form.data)
            comment.put()
            post.add_comment(comment.id)
            return "ALEYUYA"
        return "form.errors"
