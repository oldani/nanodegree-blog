from flask_user import current_user

def user_own_post(post_id):
    """ Check if a user is the owner of a post. """
    if hasattr(current_user, 'posts_list'
               ) and int(post_id) in current_user.posts_list:
        return True
    return
