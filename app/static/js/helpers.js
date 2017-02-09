var commentsTemplate = _.template(
  '<div class="card">\
    <div class="card-block">\
      <h5 class="card-title"><%= user %></h5>\
      <p class="card-text"><%= comment %></p>\
    </div>\
  </div>'
);