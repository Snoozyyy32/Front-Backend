let userName;
let password;

document.getElementById("submit-btn").onclick = function () {
    password = document.getElementById("passWord").value
    userName = document.getElementById("userName").value
    alert("welcome " + userName + ".");
}