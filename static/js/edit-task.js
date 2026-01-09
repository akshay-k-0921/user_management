$(function () {

  if (!getToken()) {
    window.location.href = "/login/";
    return;
  }

  const id = window.location.pathname.split("/")[2];

  $.ajax({
    url: API_BASE + "/tasks/" + id + "/",
    headers: authHeaders(),
    success: function (res) {
      $("#title").val(res.title);
      $("#desc").val(res.description);
    }
  });

  $("#editForm").on("submit", function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append("title", $("#title").val());
    formData.append("description", $("#desc").val());

    const fileInput = $("#file")[0];
    if (fileInput.files.length > 0) {
      formData.append("attachment", fileInput.files[0]);
    }

    $.ajax({
      url: API_BASE + "/tasks/" + id + "/",
      method: "PATCH",
      headers: authHeaders(),
      processData: false,
      contentType: false,
      data: formData,

      success: function () {
        window.location.href = "/task/" + id + "/";
      },

      error: function () {
        $("#msg").text("Failed to update task");
      }
    });
  });

});
