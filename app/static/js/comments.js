var model = {
  init: function(){
    var _self = this;
    var url = window.allCommentEndpoint || '';
    return $.getJSON(url).done(function(data) {
      _self.comments = data;
    });
  },
  comments: []
};

var controller = {
  init: function() {
    model.init().then(function() {
      view.init();
    });
  },
  getComments: function(){
    return model.comments;
  }
};

var view = {
  init:function() {
    this.commentsContainer = $("#comments");
    this.commentsTemplate = commentsTemplate;
    this.comments = controller.getComments();
    this.render();
  },
  render: function() {
    _.each(this.comments, function(item, i) {
      var commet = this.commentsTemplate(item);
      this.commentsContainer.append(commet)
    }.bind(this));
  }
};

controller.init()
