document.addEventListener('DOMContentLoaded', function () {
  // Function to update the badge count
  function updateBadgeCount(count) {
    const badge = document.querySelector('.badge');
    badge.textContent = count;
  }

  // Mock user ID
  const userId = 1;

  // API endpoint URL
  const apiUrl = `http://lojadastone.us-east-1.elasticbeanstalk.com/users/${userId}/basket/products`;

  // Make an AJAX request to the API
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      // Assuming the API response contains an array of products
      const itemCount = data.length; // Number of items in the basket
      updateBadgeCount(itemCount); // Update badge count
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
});
