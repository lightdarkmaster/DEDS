<script>
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      // User switched away from the tab
      fetch('/log_tab_switch', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ timestamp: new Date().toISOString() })
      });
    }
  });
</script>
