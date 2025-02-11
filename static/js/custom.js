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

// animations for hero-text
function restartAnimation() {
const chars = document.querySelectorAll('.char');
chars.forEach(char => {
    char.style.animation = 'none';
    void char.offsetWidth;
    char.style.animation = '';
});
}
setInterval(restartAnimation, 3000);

// about customer reviews
const emojis = document.querySelectorAll('.emoji');
emojis.forEach(emoji => {
    emoji.addEventListener('click', (e) => {
    const card = e.target.closest('.review-card');
    const thanksMessage = card.querySelector('.thanks-message');
    thanksMessage.style.display = 'block';
    setTimeout(() => {
        thanksMessage.style.display = 'none';
    }, 1500);
    });
});

// footer section