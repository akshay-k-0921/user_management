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

      $("#title").text(res.title);
      $("#desc").text(res.description);

      if (res.attachment_url) {
        $("#fileSection").html(`
          <a href="${res.attachment_url}" target="_blank" class="file-link">
            <i class="fa fa-paperclip"></i> Open Attachment
          </a>
        `);
      }
    }
  });

  $("#deleteBtn").click(function () {
    if (!confirm("Delete this task?")) return;

    $.ajax({
      url: API_BASE + "/tasks/" + id + "/",
      method: "DELETE",
      headers: authHeaders(),
      success: function () {
        window.location.href = "/home/";
      },
      error: function () {
        $("#msg").text("Failed to delete task");
      }
    });
  });

  $("#editBtn").click(function () {
    window.location.href = "/edit-task/" + id + "/";
  });

});
