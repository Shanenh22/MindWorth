// Dropdown Color Fix - Forces transparency to match text inputs
document.addEventListener('DOMContentLoaded', function() {
    const selects = document.querySelectorAll('.form-group select');
    
    selects.forEach(select => {
        // Force transparent background like text inputs
        select.style.background = 'rgba(255, 255, 255, 0.1)';
        select.style.backdropFilter = 'blur(10px)';
        select.style.color = '#FEFEFE';
        
        // Options need solid background for browser dropdown menus
        const options = select.querySelectorAll('option');
        options.forEach(option => {
            option.style.backgroundColor = '#2A2A3E';
            option.style.color = '#FEFEFE';
        });
        
        select.addEventListener('focus', function() {
            this.style.background = 'rgba(255, 255, 255, 0.15)';
            this.style.color = '#FEFEFE';
        });
        
        select.addEventListener('blur', function() {
            this.style.background = 'rgba(255, 255, 255, 0.1)';
            this.style.color = '#FEFEFE';
        });
        
        select.addEventListener('mousedown', function() {
            const options = this.querySelectorAll('option');
            options.forEach(option => {
                option.style.backgroundColor = '#2A2A3E';
                option.style.color = '#FEFEFE';
            });
        });
    });
});