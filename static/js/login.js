$(function () {

  if (getToken()) {
    window.location.href = "/home/";
    return;
  }

  $("#loginBtn").click(function () {
    $.ajax({
      url: API_BASE + "/auth/login/",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({
        identifier: $("#li_identifier").val(),
        password: $("#li_password").val()
      }),
      success: function (res) {
        if (res.access) {
          setToken(res.access);
          window.location.href = "/home/";
        } else {
          $("#msg").text("Invalid credentials");
        }
      },
      error: function () {
        $("#msg").text("Login failed");
      }
    });
  });

});
