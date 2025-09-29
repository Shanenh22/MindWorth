document.addEventListener('DOMContentLoaded', () => {
  // Dynamically create a back-to-top button for every page
  const backToTop = document.createElement('button');
  backToTop.className = 'back-to-top';
  backToTop.id = 'backToTop';
  backToTop.setAttribute('aria-label', 'Back to top');
  backToTop.innerHTML = '↑';
  document.body.appendChild(backToTop);

  // Show or hide the button based on scroll position
  window.addEventListener('scroll', () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > 500) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  });

  // Smooth scroll back to top when clicked
  backToTop.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
});