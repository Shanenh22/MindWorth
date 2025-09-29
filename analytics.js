/*
 * Google Analytics integration for MindWorth.  
 *
 * This file centralizes the Google Analytics configuration so you only need
 * to update your measurement ID in one place.  When adding additional
 * analytics or marketing pixels in the future, place them here to keep
 * your HTML documents clean and easy to maintain.
 */

// Initialize the global dataLayer if it doesn’t already exist.  Google
// Analytics uses this array to queue events before the script loads.
window.dataLayer = window.dataLayer || [];

/**
 * Pushes arguments onto the dataLayer.  This wrapper function mirrors the
 * gtag API provided by Google Analytics.  See
 * https://developers.google.com/analytics/devguides/collection/ga4 for
 * details on how to use gtag to send additional events.
 */
function gtag(){
  dataLayer.push(arguments);
}

// Record the time at which the analytics library was loaded.  This call
// ensures that Google Analytics properly timestamps subsequent events.
gtag('js', new Date());

// Configure your Google Analytics measurement ID here.  Replace
// 'G-XXXXXXXXXX' with your actual Measurement ID from the Google Analytics
// admin console.  Leaving this value unchanged will not send any data.
gtag('config', 'G-XXXXXXXXXX');
