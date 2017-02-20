from flask import jsonify, request
from flask_classy import FlaskView
from flask_user import current_user, login_required
from ..forms import CommentForm
from ..models import CommentModel, PostModel


class Comment(FlaskView):

    def get(self):
        pass

    def all(self, post_id):
        """ Retrive all the comments of a given post. """
        CommentModel.add_query_filter('post_id', '=', int(post_id))
        CommentModel.query.order = '-updated'
        return jsonify(CommentModel.fetch())

    @login_required
    def post(self, post_id):
        form = CommentForm()
        post = PostModel.get(post_id)
        if form.validate_on_submit() and post:
            comment = CommentModel(user=current_user.username,
                                   post_id=int(post_id),
                                   **form.data)
            comment.put()
            post.add_comment(comment.id)
            return jsonify(comment)
        return jsonify(form.errors), 400

    @login_required
    def delete(self, comment_id):
        post_id = request.form.get('post_id')
        if post_id:
            try:
                post = PostModel.get(post_id)
                post.delete_comment(comment_id)
            except AttributeError:
                return "You most specify a valid Post ID", 400
            CommentModel.delete(comment_id)
            return "", 204
        return "You most specify a Post ID", 400

    @login_required
    def put(self, comment_id):
        form = CommentForm()
        comment = CommentModel.get(comment_id)
        if form.validate_on_submit() and comment:
            form.populate_obj(comment)
            comment.put()
            return jsonify(comment), 201
        return jsonify(form.errors), 400
