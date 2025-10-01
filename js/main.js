/* MindWorth Solutions - Main JavaScript */

// ============================================================================
// GOOGLE SHEETS CONFIGURATION (FREE & UNLIMITED)
// ============================================================================
const GOOGLE_SHEETS_CONFIG = {
    enabled: true,  // Set to false to disable form submissions
    scriptUrl: 'https://script.google.com/macros/s/AKfycbySOHaCPS2QJTrytdbqmohCtGVuY-GssKV5VLODIzZmrl0xrMl451RpROLWMzygbXNyRQ/exec'  // Get this from Google Apps Script deployment
    // Example: 'https://script.google.com/macros/s/AKfycby.../exec'
};

// ============================================================================
// PDF DOWNLOAD MAPPING
// ============================================================================
const PDF_DOWNLOADS = {
    'checklist': 'content-creation-playbook.pdf',
    'email-checklist': 'email-admin-automation-checklist.pdf',
    'insights-guide': 'customer-insights-analysis-guide.pdf',
    'scheduling-guide': 'smart-scheduling-implementation-guide.pdf',
    'sales-playbook': 'sales-follow-up-playbook.pdf',
    'document-blueprint': 'document-processing-blueprint.pdf'
};

// ============================================================================
// Mobile Menu Toggle
// ============================================================================
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

// ============================================================================
// Modal Functions
// ============================================================================
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

// ============================================================================
// Form Submission Handler with Google Sheets Integration
// ============================================================================
function submitForm(e, type) {
    e.preventDefault();
    
    // Get form data
    const form = e.target;
    const formData = new FormData(form);
    const data = {};
    
    // Convert FormData to object
    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }
    
    // Add metadata
    data.form_type = type;
    data.page_url = window.location.href;
    data.submission_date = new Date().toISOString();
    
    // Get submit button for loading state
    const submitButton = form.querySelector('button[type="submit"]');
    const originalButtonText = submitButton.textContent;
    submitButton.textContent = type === 'audit' ? 'Scheduling...' : 'Downloading...';
    submitButton.disabled = true;
    
    console.log('Form submitted:', type, data);
    
    // ========================================================================
    // GOOGLE SHEETS SUBMISSION
    // ========================================================================
    if (GOOGLE_SHEETS_CONFIG && GOOGLE_SHEETS_CONFIG.enabled && GOOGLE_SHEETS_CONFIG.scriptUrl !== 'PASTE_YOUR_WEB_APP_URL_HERE') {
        
        fetch(GOOGLE_SHEETS_CONFIG.scriptUrl, {
            method: 'POST',
            mode: 'no-cors',  // Important! Google Apps Script requires this
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(() => {
            console.log('✅ Google Sheets submission successful');
            showSuccessMessage(type, form);
        })
        .catch(error => {
            console.error('❌ Google Sheets submission error:', error);
            // Still show success since no-cors mode can't detect errors
            showSuccessMessage(type, form);
        })
        .finally(() => {
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
        });
        
    } else {
        // Configuration not set up yet
        console.warn('⚠️ Google Sheets not configured! Update GOOGLE_SHEETS_CONFIG.scriptUrl in main.js');
        console.warn('📋 See GOOGLE-SHEETS-SETUP-COMPLETE.md for setup instructions');
        
        // Show demo success message for testing
        setTimeout(() => {
            showSuccessMessage(type, form);
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
        }, 1000);
    }
}

// ============================================================================
// Success Message Handler
// ============================================================================
function showSuccessMessage(type, form) {
    let message = '';
    let emoji = '';
    
    // Trigger PDF download if this is a lead magnet form
    if (PDF_DOWNLOADS[type]) {
        const baseLeadMagnetsDir = window.location.pathname.includes('/pages/')
        ? '../lead-magnets'
        : 'lead-magnets';

        const pdfPath = `${baseLeadMagnetsDir}/${PDF_DOWNLOADS[type]}`;
        
        // Create invisible download link and trigger it
        const downloadLink = document.createElement('a');
        downloadLink.href = pdfPath;
        downloadLink.download = PDF_DOWNLOADS[type];
        downloadLink.style.display = 'none';
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
        
        emoji = '📥';
        message = "Success! Your download is starting now. Check your email for a copy and additional resources.";
    } else if (type === 'audit') {
        emoji = '🎉';
        message = "Thank you! We'll contact you within 24 hours to schedule your free audit. Check your email for confirmation.";
    } else {
        emoji = '✅';
        message = "Thank you! We'll be in touch soon.";
    }
    
    // Create custom success modal (better UX than alert)
    const successOverlay = document.createElement('div');
    successOverlay.className = 'success-overlay';
    successOverlay.innerHTML = `
        <div class="success-message">
            <div class="success-icon">${emoji}</div>
            <h3 class="success-title">Success!</h3>
            <p class="success-text">${message}</p>
            <button class="btn-primary" onclick="closeSuccessMessage()">Got it!</button>
        </div>
    `;
    
    document.body.appendChild(successOverlay);
    
    // Animate in
    setTimeout(() => {
        successOverlay.style.opacity = '1';
        successOverlay.querySelector('.success-message').style.transform = 'translateY(0)';
    }, 10);
    
    // Reset form and close modal
    form.reset();
    closeModal(type);
    
    // Auto-close after 5 seconds
    setTimeout(() => {
        closeSuccessMessage();
    }, 5000);
}

// ============================================================================
// Close Success Message
// ============================================================================
function closeSuccessMessage() {
    const successOverlay = document.querySelector('.success-overlay');
    if (successOverlay) {
        successOverlay.style.opacity = '0';
        setTimeout(() => {
            successOverlay.remove();
        }, 300);
    }
}

// ============================================================================
// FAQ Toggle
// ============================================================================
function toggleFAQ(element) {
    element.classList.toggle('active');
}

// ============================================================================
// Smooth Scroll for Anchor Links
// ============================================================================
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

// ============================================================================
// Header Hide/Show on Scroll
// ============================================================================
document.addEventListener('DOMContentLoaded', function() {
    let lastScroll = 0;
    const header = document.querySelector('header');
    const scrollThreshold = 100;

    if (header) {
        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
            
            // Always show header at the very top
            if (currentScroll <= 50) {
                header.classList.remove('scroll-down');
                header.classList.remove('scroll-up');
                header.style.transform = 'translateY(0)';
                lastScroll = currentScroll;
                return;
            }
            
            // Hide header when scrolling down past threshold
            if (currentScroll > lastScroll && currentScroll > scrollThreshold) {
                header.classList.add('scroll-down');
                header.classList.remove('scroll-up');
                header.style.transform = 'translateY(-100%)';
            } 
            // Show header when scrolling up
            else if (currentScroll < lastScroll) {
                header.classList.remove('scroll-down');
                header.classList.add('scroll-up');
                header.style.transform = 'translateY(0)';
            }
            
            lastScroll = currentScroll;
        });
    }
});

// ============================================================================
// Intersection Observer for Fade-in Animations
// ============================================================================
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

// ============================================================================
// Form Validation Helper
// ============================================================================
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

// ============================================================================
// Console Messages
// ============================================================================
console.log('%cWelcome to MindWorth Solutions!', 'color: #06D6A0; font-size: 20px; font-weight: bold;');
console.log('%cBuilding the future of small business automation', 'color: #8B5CF6; font-size: 14px;');

// Check if Google Sheets is configured
if (GOOGLE_SHEETS_CONFIG.scriptUrl === 'PASTE_YOUR_WEB_APP_URL_HERE') {
    console.warn('%c⚠️ SETUP REQUIRED: Google Sheets not configured', 'color: #FFD60A; font-size: 14px; font-weight: bold;');
    console.log('%c📋 Follow the setup guide: GOOGLE-SHEETS-SETUP-COMPLETE.md', 'color: #06D6A0; font-size: 12px;');
} else {
    console.log('%c✅ Google Sheets configured and ready!', 'color: #06D6A0; font-size: 14px; font-weight: bold;');
}