// form validation
$("#id_first_name").keyup(function () {
  var $this = $(this);

  if ($("#validate_avatar_id_first_name").length == 0) {
    var $ve = $("<span />");
    $ve.attr('id', 'validate_avatar_id_first_name');
    $ve.text("validating...");
    $(this).after($ve);
  }

  $.post(
    '/validate',
    {field_value: $this.val(),
     field_name: 'first_name',
     csrfmiddlewaretoken: csrfToken},
     function (data) {
        console.log(data);
        $("#validate_avatar_id_first_name").text(data.result);
     });
});