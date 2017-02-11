from flask import jsonify, request
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
        comment.query.order = '-updated'
        return jsonify(comment.fetch())

    @login_required
    def post(self, post_id):
        form = CommentForm()
        if form.validate_on_submit():
            post = PostModel().get(post_id)
            post = PostModel(**post)
            comment = CommentModel(user=current_user.username,
                                   post_id=int(post_id),
                                   **form.data)
            comment.put()
            post.add_comment(comment.id)
            return jsonify(comment.data)
        return "form.errors"

    @login_required
    def delete(self, comment_id):
        post_id = request.form.get('post_id')
        if post_id:
            # CommentModel().delete(comment_id)
            # post = PostModel().get(post_id)
            # post.delete_comment(comment_id)
            return "", 200
        return "hola"
        # comment = CommentModel()
        # comment = comment.get(post_id)
        # print(comment)
