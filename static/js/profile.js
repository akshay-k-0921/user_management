$(function () {

  if (!getToken()) {
    window.location.href = "/login/";
    return;
  }

  $.ajax({
    url: API_BASE + "/auth/profile/",
    headers: authHeaders(),
    success: function (res) {
      const d = res.data;

      $("#email").val(d.email || "");
      $("#full_name").val(d.full_name || "");
      $("#dob").val(d.dob || "");
      $("#address").val(d.address || "");
      $("#gender").val(d.gender || "");
      $("#mobile").val(d.mobile_number || "");
    }
  });

  $("#saveBtn").click(function () {

    const dobVal = $("#dob").val();

    const payload = {
      full_name: $("#full_name").val(),
      address: $("#address").val(),
      gender: $("#gender").val(),
      mobile_number: $("#mobile").val()
    };

    if (dobVal) {
      payload.dob = dobVal;
    }

    $.ajax({
      url: API_BASE + "/auth/profile/",
      method: "PATCH",
      headers: {
        ...authHeaders(),
        "Content-Type": "application/json"
      },
      data: JSON.stringify(payload),
      success: function () {
        $("#msg").text("Profile updated successfully");
      },
      error: function () {
        $("#msg").text("Failed to update profile");
      }
    });
  });

  $("#goResetPwdBtn").click(function () {
    window.location.href = "/reset-password/";
  });

});
