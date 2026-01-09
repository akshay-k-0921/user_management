const API_BASE = "http://127.0.0.1:8000/api";

function getToken() {
  return localStorage.getItem("access");
}

function setToken(token) {
  localStorage.setItem("access", token);
}

function logout() {
  localStorage.removeItem("access");
  window.location.href = "/login/";
}

function authHeaders() {
  return {
    "Authorization": "Bearer " + getToken()
  };
}

$(document).ajaxError(function (event, xhr) {
  if (xhr.status === 401) {
    logout();
  }
});
