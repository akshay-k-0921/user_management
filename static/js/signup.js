$(function () {

  if (getToken()) {
    window.location.href = "/home/";
    return;
  }

  $("#signupBtn").click(function () {
    $.ajax({
      url: API_BASE + "/auth/register/",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({
        username: $("#su_username").val(),
        email: $("#su_email").val(),
        password: $("#su_password").val()
      }),
      success: function () {
        window.location.href = "/login/";
      },
      error: function () {
        $("#msg").text("Signup failed");
      }
    });
  });

});
