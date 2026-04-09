const products = [
  { src: "https://www.notebookcheck.net/fileadmin/Notebooks/Lenovo/ThinkPad_X1_Carbon_2017-20HQS03P00_/teaser_4_3.JPG", name: "Laptop", price: 999, brand: "Lenovo" },
  { src: "https://media.krefel.be/sys-master/products/9464104943646/3840x3840.51007028_01.webp", name: "Phone", price: 699, brand: "Samsung" },
  { src: "https://fonez.ie/cdn/shop/files/iPadPro12.9_5thGeneration_Cellularsilver_4def963f-61a1-4470-bb68-afe905398cfe.webp?v=1697025804&width=850", name: "Tablet", price: 399, brand: "Apple" },
  { src: "https://www.mcsteve.com/wp-content/uploads/2021/04/sony-xm4-1.png", name: "Headphones", price: 200, brand: "Sony" },
  { src: "https://m.media-amazon.com/images/I/71tjy7Umf0L._AC_SL1500_.jpg", name: "Watch", price: 150, brand: "Garmin" },
  { src: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6470/6470245cv12d.jpg", name: "TV", price: 1500, brand: "Google" },
  { src: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6426/6426149_sd.jpg", name: "Console", price: 400, brand: "Sony" },
  { src: "https://images.techhive.com/images/article/2013/05/microsoft_sculpt_mobile_mouse_left_2013-100038808-orig.jpg", name: "Mouse", price: 90, brand: "Windows" },
  { src: "https://www.bhphotovideo.com/images/images2500x2500/asus_pa279crv_27_4k_hdr_uhd_1762484.jpg", name: "Monitor", price: 350, brand: "ASUS" }
];

const cartKey = "cart";
const box = document.getElementById("products");
const cartCountElement = document.getElementById("cart-count");

function loadCart() {
  return JSON.parse(localStorage.getItem(cartKey)) || [];
}

function saveCart(cart) {
  localStorage.setItem(cartKey, JSON.stringify(cart));
}

function updateCartCount() {
  if (!cartCountElement) return;
  const totalItems = loadCart().reduce((sum, item) => sum + item.quantity, 0);
  cartCountElement.textContent = totalItems;
}

function addToCart(index) {
  const cart = loadCart();
  const product = products[index];
  const existing = cart.find(item => item.name === product.name);

  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ ...product, quantity: 1 });
  }

  saveCart(cart);
  updateCartCount();
  alert(`${product.name} added to cart.`);
}

function checkOut() {
  window.location.href = "checkOut.html";
}

function renderProducts() {
  let output = "";

  for (let i = 0; i < products.length; i++) {
    const item = products[i];
    output += `
      <div class="infobox">
        <img src="${item.src}" alt="${item.name}" width="150" height="100">
        <h3>${item.name}</h3>
        <p>Brand: ${item.brand}</p>
        <p>Price: $${item.price}</p>
        <button onclick="addToCart(${i})">Add to Cart</button>
      </div>
    `;
  }

  box.innerHTML = output;
}

renderProducts();
updateCartCount();
