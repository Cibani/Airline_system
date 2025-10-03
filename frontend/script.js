const API = 'http://localhost:8080/api';
let user = JSON.parse(localStorage.getItem('user')) || null;

document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.includes('index.html') && !user) {
        window.location.href = 'login.html';
        return;
    }
    if (user && window.location.pathname.includes('index.html')) {
        document.getElementById('username').textContent = user.username;
    }

    //
