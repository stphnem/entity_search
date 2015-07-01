$('a[rel=popover]').popover({
  html: true,
  placement: 'bottom',
  trigger: 'hover',
  content: function () {
    return '<img src="'+$(this).data('img') + '" />';
  }
});