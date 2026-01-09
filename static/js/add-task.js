$(function () {

  if (!getToken()) {
    window.location.href = "/login/";
    return;
  }

  $("#taskForm").on("submit", function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append("title", $("#title").val());
    formData.append("description", $("#desc").val());

    const fileInput = $("#file")[0];
    if (fileInput.files.length > 0) {
      formData.append("attachment", fileInput.files[0]);
    }

    $.ajax({
      url: API_BASE + "/tasks/",
      method: "POST",
      headers: authHeaders(),
      processData: false,
      contentType: false,
      data: formData,

      success: function () {
        window.location.href = "/home/";
      },

      error: function (xhr) {
        console.log(xhr.responseJSON);
        $("#msg").text("Failed to create task");
      }
    });

  });

});
