const cartKey = "cart";
const cartItemsEl = document.getElementById("cart-items");
const subtotalEl = document.getElementById("subtotal");
const totalEl = document.getElementById("total");
const form = document.getElementById("checkout-form");
const taxRate = 0.1;

function loadCart() {
  return JSON.parse(localStorage.getItem(cartKey)) || [];
}

function saveCart(cart) {
  localStorage.setItem(cartKey, JSON.stringify(cart));
}

function formatPrice(value) {
  return value.toFixed(2);
}

function calculateTotals(cart) {
  const subtotal = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const tax = subtotal * taxRate;
  return {
    subtotal,
    tax,
    total: subtotal + tax,
  };
}

function renderCart() {
  const cart = loadCart();
  const mainButton = form.querySelector("button[type='submit']");

  if (!cart.length) {
    cartItemsEl.innerHTML = `<div class="empty-cart">Your shopping cart is empty.</div>`;
    subtotalEl.textContent = "0.00";
    totalEl.textContent = "0.00";
    if (mainButton) mainButton.disabled = true;
    return;
  }

  if (mainButton) mainButton.disabled = false;

  cartItemsEl.innerHTML = cart
    .map((item, index) => `
      <div class="cart-row">
        <img src="${item.src}" alt="${item.name}" />
        <div>
          <p><strong>${item.name}</strong></p>
          <p>${item.brand}</p>
        </div>
        <p>$${formatPrice(item.price)}</p>
        <input type="number" min="1" value="${item.quantity}" onchange="changeQuantity(${index}, this.value)" />
        <button type="button" onclick="removeItem(${index})">Remove</button>
      </div>
    `)
    .join("");

  const totals = calculateTotals(cart);
  subtotalEl.textContent = formatPrice(totals.subtotal);
  totalEl.textContent = formatPrice(totals.total);
}

function changeQuantity(index, value) {
  const cart = loadCart();
  const quantity = Number(value);

  if (!Number.isInteger(quantity) || quantity < 1) {
    removeItem(index);
    return;
  }

  cart[index].quantity = quantity;
  saveCart(cart);
  renderCart();
}

function removeItem(index) {
  const cart = loadCart();
  cart.splice(index, 1);
  saveCart(cart);
  renderCart();
}

function submitOrder() {
  const cart = loadCart();
  if (!cart.length) {
    alert("Your cart is empty. Add items before placing an order.");
    return false;
  }

  const name = document.getElementById("customer-name").value.trim();
  const email = document.getElementById("customer-email").value.trim();
  const address = document.getElementById("customer-address").value.trim();
  const payment = document.getElementById("customer-payment").value;

  if (!name || !email || !address) {
    alert("Please fill in all shipping details before placing your order.");
    return false;
  }

  const totals = calculateTotals(cart);
  alert(
    `Thank you, ${name}!\n\nOrder summary:\n${cart.length} item(s)\nTotal: $${formatPrice(totals.total)}\nPayment method: ${payment}\n\nYour order has been placed successfully!`
  );

  localStorage.removeItem(cartKey);
  renderCart();
  form.reset();
  return false;
}

window.changeQuantity = changeQuantity;
window.removeItem = removeItem;
window.submitOrder = submitOrder;

renderCart();
