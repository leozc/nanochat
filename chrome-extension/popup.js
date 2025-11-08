document.addEventListener('DOMContentLoaded', function() {
  const copyBtn = document.getElementById('copyBtn');
  const status = document.getElementById('status');
  const urlDisplay = document.getElementById('urlDisplay');

  // Display current URL on popup load
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    if (tabs[0] && tabs[0].url) {
      urlDisplay.textContent = tabs[0].url;
    }
  });

  copyBtn.addEventListener('click', function() {
    // Get the current active tab
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      if (tabs[0] && tabs[0].url) {
        const url = tabs[0].url;

        // Copy to clipboard
        navigator.clipboard.writeText(url).then(function() {
          // Show success message
          status.textContent = 'URL copied to clipboard!';
          status.className = 'status success';
          status.classList.remove('hidden');

          // Hide status message after 2 seconds
          setTimeout(function() {
            status.classList.add('hidden');
          }, 2000);
        }).catch(function(err) {
          // Show error message
          status.textContent = 'Failed to copy URL';
          status.className = 'status error';
          status.classList.remove('hidden');
          console.error('Copy failed:', err);
        });
      }
    });
  });
});
