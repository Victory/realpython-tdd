// form validation

$("form input[type=text]").each(function () {
  $(this).keyup(function () {
    var $this = $(this);
    var fieldValue = $this.val();
    var fieldName = $this.attr('name');
    var avatarPrefix = "validate_avatar_";
    var avatarSuffix = $this.attr('id');
    var avatarId = avatarPrefix + avatarSuffix;
    var $avatar = $("#" + avatarId);

    if ($avatar.length === 0) {
      $avatar = $("<span />");
      $avatar.attr('id', avatarId);
      $this.after($avatar);
    }

    $avatar.text("validating...");

    $.post(
      '/validate',
      {field_value: fieldValue,
       field_name: fieldName,
       csrfmiddlewaretoken: csrfToken},
      function (data) {
        $avatar.text(data.result);
      });
  });
});