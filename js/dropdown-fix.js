// Dropdown Color Fix - Forces correct colors on all browsers
// Add this script to your HTML page

document.addEventListener('DOMContentLoaded', function() {
    // Get all select elements in form groups
    const selects = document.querySelectorAll('.form-group select');
    
    selects.forEach(select => {
        // Force inline styles on the select element
        select.style.backgroundColor = '#555555 ';
        select.style.color = '#FEFEFE';
        
        // Apply styles to all options
        const options = select.querySelectorAll('option');
        options.forEach(option => {
            option.style.backgroundColor = '#555555  ';
            option.style.color = '#FEFEFE';
        });
        
        // Handle focus/blur events
        select.addEventListener('focus', function() {
            this.style.backgroundColor = '#555555';
            this.style.color = '#FEFEFE';
        });
        
        select.addEventListener('blur', function() {
            this.style.backgroundColor = '#555555';
            this.style.color = '#FEFEFE';
        });
        
        // Re-apply styles when dropdown opens (Chrome/Safari)
        select.addEventListener('mousedown', function() {
            const options = this.querySelectorAll('option');
            options.forEach(option => {
                option.style.backgroundColor = '#555555';
                option.style.color = '#FEFEFE';
            });
        });
    });
});