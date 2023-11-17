// Function to remove a product from the shopping cart
async function removeProductFromCart(product_id) {
  const user_id = 1; // Mock user ID
  const removeUrl = `http://lojadastone.us-east-1.elasticbeanstalk.com/baskets/${user_id}/products/${product_id}`;

  try {
    const response = await fetch(removeUrl, {
      method: 'DELETE',
    });

    if (response.ok) {
      // Remove the product card from the UI
      const productCard = document.getElementById(`productCard_${product_id}`);
      productCard.remove();
    } else {
      console.error(
        'Erro ao remover o produto do carrinho:',
        response.statusText
      );
    }
  } catch (error) {
    console.error('Erro ao remover o produto do carrinho:', error);
  }
}

// Function to fetch user's shopping cart data and populate the cart.html page
async function populateCart() {
  const user_id = 1; // Mock user ID
  const cartUrl = `http://lojadastone.us-east-1.elasticbeanstalk.com/users/${user_id}/basket/products`;

  try {
    const response = await fetch(cartUrl);
    const cartData = await response.json();

    const cartContainer = document.querySelector('.row-cols-2');

    cartData.forEach((product) => {
      const productCard = document.createElement('div');
      productCard.className = 'col mb-5';
      productCard.id = `productCard_${product.id}`; // Set a unique ID for each product card
      productCard.innerHTML = `
              <div class="card h-100">
                  <div class="card-body">
                      <h4 class="card-title">${product.name}</h4>
                      <p class="card-text">${product.description}</p>
                      <p class="card-text">${product.quantity} unidade(s)</p>
                      <button class="btn btn-danger" onclick="removeProductFromCart(${product.id})">Tirar do carrinho</button>
                  </div>
              </div>
          `;
      cartContainer.appendChild(productCard);
    });
  } catch (error) {
    console.error('Erro ao buscar os dados do carrinho:', error);
  }
}

// Call the populateCart function when the page loads
document.addEventListener('DOMContentLoaded', populateCart);
