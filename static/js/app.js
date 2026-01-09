const API_BASE = "https://user-management-6o4y.onrender.com/api";

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
