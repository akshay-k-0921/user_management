$(function () {

  if (!getToken()) {
    window.location.href = "/login/";
    return;
  }

  $("#resetBtn").click(function () {

    const payload = {
      old_password: $("#old_password").val(),
      new_password: $("#new_password").val(),
      confirm_password: $("#confirm_password").val()
    };

    $("#msg").html("");

    $.ajax({
      url: API_BASE + "/auth/change-password/",
      method: "PATCH",
      headers: {
        ...authHeaders(),
        "Content-Type": "application/json"
      },
      data: JSON.stringify(payload),

      success: function () {
        $("#msg").css("color", "green");
        $("#msg").text("Password updated successfully");
        setTimeout(function () {
          window.location.href = "/profile/";
        }, 1200);
      },

      error: function (xhr) {
        let msg = "Failed to reset password";

        if (xhr.responseJSON) {
          if (xhr.responseJSON.non_field_errors) {
            msg = xhr.responseJSON.non_field_errors.join("<br>");
          } else if (xhr.responseJSON.message) {
            msg = xhr.responseJSON.message;
          } else {
            msg = Object.values(xhr.responseJSON).flat().join("<br>");
          }
        }

        $("#msg").css("color", "red");
        $("#msg").html(msg);
      }
    });

  });

});
