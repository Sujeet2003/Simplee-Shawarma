// Select all navigation links
const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', function () {
        navLinks.forEach(nav => nav.classList.remove('active'));
        this.classList.add('active');
    });
});

// To turn off the toggle navbar while clicking anywhere on screen
document.addEventListener('click', function (event) {
    const navbarCollapse = document.getElementById('navbarNav');
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarCollapse.classList.contains('show') &&
        !navbarCollapse.contains(event.target) &&
        !navbarToggler.contains(event.target)) {
        new bootstrap.Collapse(navbarCollapse).hide();
    }
});

// to change the navbar background
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('mainNavbar');
    if (window.scrollY > window.innerHeight) {
        navbar.classList.remove('bg-transparent');
        navbar.classList.add('bg-dark');
    } else {
        navbar.classList.add('bg-transparent');
        navbar.classList.remove('bg-dark');
    }
});

// animations for hero-text
function restartAnimation() {
const chars = document.querySelectorAll('.char');
chars.forEach(char => {
    char.style.animation = 'none';
    void char.offsetWidth;
    char.style.animation = '';
});
}
setInterval(restartAnimation, 4000);