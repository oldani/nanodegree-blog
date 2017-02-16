// Save templates to global vars.

var commentsTemplate = _.template(
  $(".comments-template").html() || ''
);

var errorTemplate = _.template(
  $(".error-template").html() || ''
);
