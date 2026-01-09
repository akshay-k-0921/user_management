$(function () {

  if (!getToken()) {
    window.location.href = "/login/";
    return;
  }

  let currentPage = 1;

  loadTasks();

  $("#filterBtn").click(function () {
    currentPage = 1;
    loadTasks();
  });

  function loadTasks() {
    const search = $("#search").val();
    const order = $("#order").val();

    let url = API_BASE + "/tasks/?page=" + currentPage;

    if (search) url += "&search=" + encodeURIComponent(search);
    if (order) url += "&ordering=" + order;

    $.ajax({
      url: url,
      headers: authHeaders(),
      success: function (res) {

        const tasks = res.results || [];

        let html = "";
        tasks.forEach(t => {

          const fileIcon = t.attachment_url
            ? `<a href="${t.attachment_url}" target="_blank" class="file-icon">
                 <i class="fa fa-paperclip"></i>
               </a>`
            : "";

          html += `
            <li class="task-item">
              <div class="task-main">
                <a href="/task/${t.id}/">${t.title}</a>
                ${fileIcon}
              </div>
              <div class="task-actions">
                <span class="date">
                  ${new Date(t.created_at).toLocaleDateString()}
                </span>
                <i class="fa fa-pen edit-icon" data-id="${t.id}"></i>
                <i class="fa fa-trash delete-icon" data-id="${t.id}"></i>
              </div>
            </li>
          `;
        });

        $("#taskList").html(html || "<p>No tasks found</p>");
        bindActions();
        renderPagination(res);
      }
    });
  }

  function bindActions() {

    $(".delete-icon").click(function () {
      const id = $(this).data("id");
      if (!confirm("Delete this task?")) return;

      $.ajax({
        url: API_BASE + "/tasks/" + id + "/",
        method: "DELETE",
        headers: authHeaders(),
        success: function () {
          loadTasks();
        }
      });
    });

    $(".edit-icon").click(function () {
      const id = $(this).data("id");
      window.location.href = "/edit-task/" + id + "/";
    });
  }

  function renderPagination(res) {
    let html = "";

    if (res.previous) html += `<button id="prevBtn">Previous</button>`;
    html += `<span class="page-info">Page ${currentPage}</span>`;
    if (res.next) html += `<button id="nextBtn">Next</button>`;

    $("#pagination").html(html);

    $("#prevBtn").click(function () {
      if (currentPage > 1) {
        currentPage--;
        loadTasks();
      }
    });

    $("#nextBtn").click(function () {
      currentPage++;
      loadTasks();
    });
  }

});
