(function() {
  var model = {
    init: function(){
      var url = window.allCommentEndpoint || '';
      return $.getJSON(url).done(function(data) {
        this.comments = data;
      }.bind(this));
    },
    comments: []
  };

  var controller = {
    init: function() {
      model.init().then(function() {
        commentsView.init();
      });
      formView.init();
    },
    getComments: function(){
      return model.comments;
    },
    updateComments: function(comment) {
      model.comments = [comment].concat(model.comments);
      commentsView.reRender();
    },
    deleteComment: function(commentId) {
      model.comments = _.reject(model.comments, function(comment) {
        return comment.id == commentId;
      });
    }
  };

  var commentsView = {
    init: function() {
      this.currentUser = window.currentUser;
      this.deleteEndpoint = window.commentDeleteEndpoint;

      this.$commentsContainer = $(".comments");
      this.commentsTemplate = commentsTemplate;

      this.comments = controller.getComments();

      this.render();

      this.$commentsContainer.on('click', '.delete-comment', function(e) {
        e.preventDefault();
        this.deleteComment(e.target.href);
      }.bind(this));
    },
    render: function() {
      this.$commentsContainer.html('');
      _.each(this.comments, function(item, i) {
        item.currentUser = this.currentUser;
        item.deleteUrl = this.deleteEndpoint.concat(item.id);

        var comment = this.commentsTemplate(item);
        this.$commentsContainer.append(comment);

      }.bind(this));

      this.$commentsContainer.fadeIn("slow");
    },
    reRender: function() {
      this.$commentsContainer.fadeOut("slow");
      this.comments = controller.getComments();
      this.render();
    },
    deleteComment: function(targetUrl) {
      var postId = _.last(window.commentPostEnpoint.split('/'));
      $.ajax(targetUrl, {
        method: "DELETE",
        data: {'post_id': postId}
      })
      .done(function(){
        commentId = _.last(targetUrl.split("/"));

        controller.deleteComment(commentId);
        this.reRender();

      }.bind(this));
    }
  };

  var formView = {
    init: function(){
      var postEnpoint = window.commentPostEnpoint || '';
      var form = $(".comment-form form");

      form.submit(function(e) {
        e.preventDefault();

        var $this, data;

        $this = $(this);
        data = $this.serializeArray();

        $.post(postEnpoint, data).done(function(data) {
          $this.find("#comment").val("");
          controller.updateComments(data);
        });
      });
    },
  };

  controller.init();
})();
