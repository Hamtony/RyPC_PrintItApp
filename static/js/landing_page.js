window.addEventListener('scroll', () => {
    const header = document.getElementById('header');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Detecta el evento de scroll
window.addEventListener('scroll', function() {
    const mainContent = document.querySelector('.main-content');
    if (window.scrollY > 10) {
      mainContent.classList.add('scroll-effect');
    } else {
      mainContent.classList.remove('scroll-effect');
    }
});