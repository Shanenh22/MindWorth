/* MindWorth AI - Main JavaScript */

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileToggle = document.getElementById('mobileToggle');
    const mobileMenu = document.getElementById('mobileMenu');

    if (mobileToggle && mobileMenu) {
        mobileToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            
            // Animate hamburger lines
            const lines = mobileToggle.querySelectorAll('.hamburger-line');
            if (mobileMenu.classList.contains('active')) {
                lines[0].style.transform = 'rotate(45deg) translateY(10px)';
                lines[1].style.opacity = '0';
                lines[2].style.transform = 'rotate(-45deg) translateY(-10px)';
            } else {
                lines[0].style.transform = 'none';
                lines[1].style.opacity = '1';
                lines[2].style.transform = 'none';
            }
        });

        // Close mobile menu when clicking on links
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
                const lines = mobileToggle.querySelectorAll('.hamburger-line');
                lines[0].style.transform = 'none';
                lines[1].style.opacity = '1';
                lines[2].style.transform = 'none';
            });
        });
    }
});

// Modal Functions
function openModal(type) {
    const modal = document.getElementById(type + 'Modal');
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal(type) {
    const modal = document.getElementById(type + 'Modal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Close modal when clicking outside
document.addEventListener('DOMContentLoaded', function() {
    const modals = document.querySelectorAll('.modal');
    
    modals.forEach(modal => {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                const modalType = modal.id.replace('Modal', '');
                closeModal(modalType);
            }
        });
    });

    // Close modal on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            modals.forEach(modal => {
                if (modal.classList.contains('active')) {
                    const modalType = modal.id.replace('Modal', '');
                    closeModal(modalType);
                }
            });
        }
    });
});

// Form Submission Handler
function submitForm(e, type) {
    e.preventDefault();
    
    // Get form data
    const form = e.target;
    const formData = new FormData(form);
    const data = {};
    
    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }
    
    // Log for development
    console.log('Form submitted:', type, data);
    
    // Show success message
    let message = '';
    if (type === 'audit') {
        message = "Thank you! We'll contact you within 24 hours to schedule your free audit.";
    } else if (type === 'checklist') {
        message = "Thank you! Check your email for the checklist download link.";
    } else {
        message = "Thank you! We'll be in touch soon.";
    }
    
    alert(message);
    
    // Reset form and close modal
    form.reset();
    closeModal(type);
    
    // Here you would typically send data to your backend/email service
    // Example:
    // sendToBackend(type, data);
}

// FAQ Toggle
function toggleFAQ(element) {
    element.classList.toggle('active');
}

// Smooth Scroll for Anchor Links
document.addEventListener('DOMContentLoaded', function() {
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Don't prevent default for links that just open modals
            if (href === '#' || this.hasAttribute('onclick')) {
                return;
            }
            
            e.preventDefault();
            
            const target = document.querySelector(href);
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Header Hide/Show on Scroll
let lastScroll = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll <= 0) {
        header.classList.remove('scroll-up');
        return;
    }
    
    if (currentScroll > lastScroll && !header.classList.contains('scroll-down')) {
        // Scroll down
        header.classList.remove('scroll-up');
        header.classList.add('scroll-down');
    } else if (currentScroll < lastScroll && header.classList.contains('scroll-down')) {
        // Scroll up
        header.classList.remove('scroll-down');
        header.classList.add('scroll-up');
    }
    
    lastScroll = currentScroll;
});

// Intersection Observer for Fade-in Animations
document.addEventListener('DOMContentLoaded', function() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe cards and sections
    const animatedElements = document.querySelectorAll('.card, .problem-card, .step, .automation-category');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Form Validation Helper
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return false;
    
    const emailInput = form.querySelector('input[type="email"]');
    const requiredInputs = form.querySelectorAll('[required]');
    
    let isValid = true;
    
    // Check required fields
    requiredInputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = 'var(--sunset-coral)';
        } else {
            input.style.borderColor = 'var(--electric-purple)';
        }
    });
    
    // Validate email format
    if (emailInput && emailInput.value && !validateEmail(emailInput.value)) {
        isValid = false;
        emailInput.style.borderColor = 'var(--sunset-coral)';
    }
    
    return isValid;
}

// Console welcome message
console.log('%cWelcome to MindWorth AI!', 'color: #06D6A0; font-size: 20px; font-weight: bold;');
console.log('%cBuilding the future of small business automation', 'color: #8B5CF6; font-size: 14px;');