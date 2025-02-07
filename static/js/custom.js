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
// Get the modal and its components
const modal = document.getElementById("modal");
const modalText = document.getElementById("modal-text");
const closeModal = document.getElementById("close-modal");

// Get all list items
const listItems = document.querySelectorAll("ul.d-flex li");

// Add click event listeners to each list item
listItems.forEach(item => {
    item.addEventListener("click", () => {
        // Set the modal content based on the clicked item's data-content attribute
        modalText.textContent = item.getAttribute("data-content");
        // Display the modal
        modal.style.display = "block";
    });
});

// Close the modal when the close button is clicked
closeModal.addEventListener("click", () => {
    modal.style.display = "none";
});

// Close the modal when clicking outside of it
window.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});