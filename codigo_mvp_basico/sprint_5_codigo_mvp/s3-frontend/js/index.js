// Fetch products from the provided endpoint
fetch('http://lojadastone.us-east-1.elasticbeanstalk.com/products')
  .then((response) => response.json())
  .then((products) => {
    const productContainer = document.querySelector('.row-cols-2'); // Select the container where products will be displayed

    // Loop through the products and generate product cards
    products.forEach((product) => {
      const card = document.createElement('div');
      card.className = 'col mb-5';
      card.innerHTML = `
                <div class="card h-100">
                    <img class="card-img-top" src="/assets/${
                      product.image
                    }" alt="${product.name}" />
                    <div class="card-body p-4">
                        <div class="text-center">
                            <h5 class="fw-bolder">${product.name}</h5>
                            <p>${product.description}</p>
                            $${product.price.toFixed(2)}
                        </div>
                    </div>
                    <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                        <div class="text-center">
                            <input class="my-2" type="number" id="quantity_${
                              product.id
                            }" min="1" value="1">
                            <button class="btn btn-outline-dark mt-auto" onclick="addToCart(${
                              product.id
                            })">Adicionar ao carrinho</button>
                        </div>
                    </div>
                </div>
            `;

      productContainer.appendChild(card);
    });
  })
  .catch((error) => console.error('Error fetching products:', error));

// Function to add a product to the user's basket with a specific quantity
function addToCart(product_id) {
  const user_id = 1; // Mock user ID
  const quantity = document.getElementById(`quantity_${product_id}`).value; // Get the selected quantity
  const addUrl = `http://lojadastone.us-east-1.elasticbeanstalk.com/baskets/${user_id}/products`;

  // Send a POST request to add the product to the cart
  fetch(addUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      product_id: product_id,
      quantity: quantity,
    }),
  })
    .then((response) => {
      if (response.ok) {
        // Handle success, for example, show a success message
        console.log('Product added to cart successfully!');

        // Update cart count
        const cartCountBadge = document.querySelector('.badge');
        const currentCount = parseInt(cartCountBadge.textContent);
        cartCountBadge.textContent = currentCount + 1;

        // Show alert
        showAlert('Produto adicionado ao carrinho!', 'success');
      } else {
        // Handle error, for example, show an error message
        console.error('Error adding product to cart:', response.statusText);
        showAlert('Erro ao adicionar produto ao carrinho.', 'error');
      }
    })
    .catch((error) => {
      console.error('Error adding product to cart:', error);
      showAlert('Erro ao adicionar produto ao carrinho.', 'error');
    });
}

// Function to display an alert
function showAlert(message, type) {
  const alertDiv = document.createElement('div');
  alertDiv.className = `alert alert-${type}`;
  alertDiv.textContent = message;

  const container = document.querySelector('.store-container');
  container.insertBefore(alertDiv, container.firstChild);

  // Remove the alert after 3 seconds
  setTimeout(() => {
    alertDiv.remove();
  }, 3000);
}
