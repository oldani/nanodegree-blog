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
      model.comments = model.comments.concat(comment);
      commentsView.reRender();
    }
  };

  var commentsView = {
    init: function() {
      this.$commentsContainer = $(".comments");
      this.commentsTemplate = commentsTemplate;
      this.comments = controller.getComments();
      this.render();
    },
    render: function() {
      this.$commentsContainer.html('');
      _.each(this.comments, function(item, i) {
        var comment = this.commentsTemplate(item);
        this.$commentsContainer.append(comment);
      }.bind(this));
      this.$commentsContainer.fadeIn("slow");
    },
    reRender: function() {
      this.$commentsContainer.fadeOut("slow");
      this.comments = controller.getComments();
      this.render();
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
