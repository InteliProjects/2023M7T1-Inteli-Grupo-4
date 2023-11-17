document.addEventListener("DOMContentLoaded", function () {
  const paymentForm = document.getElementById("paymentForm");

  const errorMessage = "Erro no pagamento. Tente novamente mais tarde.";
  const successMessage = "Pagamento bem-sucedido! Obrigado por sua compra.";

  const errorButton = document.querySelector(".btn.btn-danger");
  const successButton = document.querySelector(".btn.btn-success");

  errorButton.addEventListener("click", function () {
    showAlert(errorMessage, "danger");
  });

  successButton.addEventListener("click", function () {
    showAlert(successMessage, "success");
  });

  paymentForm.addEventListener("submit", function (e) {
    e.preventDefault();
  });

  // Function to display an alert
  function showAlert(message, type) {
    const alertDiv = document.createElement("div");
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;

    const container = document.querySelector("#paymentForm");
    container.insertBefore(alertDiv, container.firstChild);

    // Remove the alert after 3 seconds
    setTimeout(() => {
      alertDiv.remove();
    }, 3000);
  }
});
