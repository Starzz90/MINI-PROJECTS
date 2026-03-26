const products = [
  { src : "https://www.notebookcheck.net/fileadmin/Notebooks/Lenovo/ThinkPad_X1_Carbon_2017-20HQS03P00_/teaser_4_3.JPG" , name: "Laptop", price: 999, brand: "Lenovo", buy : "buy"},
  { src : "https://media.krefel.be/sys-master/products/9464104943646/3840x3840.51007028_01.webp" , name: "Phone", price: 699, brand: "Samsung", buy : "buy" },
  { src : "https://fonez.ie/cdn/shop/files/iPadPro12.9_5thGeneration_Cellularsilver_4def963f-61a1-4470-bb68-afe905398cfe.webp?v=1697025804&width=850", name: "Tablet", price: 399, brand: "Apple", buy: "buy" },
  { src : "https://www.mcsteve.com/wp-content/uploads/2021/04/sony-xm4-1.png", name: "Headphones", price: 200, brand: "Sony", buy: "buy"},
   { src : "https://m.media-amazon.com/images/I/71tjy7Umf0L._AC_SL1500_.jpg", name: "Watch", price: 150, brand: "Garmin", buy: "buy"},
    { src : "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6470/6470245cv12d.jpg", name: "TV", price: 1500, brand: "Google", buy: "buy"},
     { src : "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6426/6426149_sd.jpg", name: "Console", price: 400, brand: "Sony", buy: "buy"},
      { src : "https://images.techhive.com/images/article/2013/05/microsoft_sculpt_mobile_mouse_left_2013-100038808-orig.jpg", name: "Mouse", price: 90, brand: "Windows", buy: "buy"},
       { src : "https://www.bhphotovideo.com/images/images2500x2500/asus_pa279crv_27_4k_hdr_uhd_1762484.jpg", name: "Monitor", price: 350, brand: "ASUS", buy: "buy"},
];

// Find the place on the page
const box = document.getElementById("products");
function increaseQty(index) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    cart[index].quantity += 1;

    localStorage.setItem("cart", JSON.stringify(cart));
    displayCart();
}
function getTotal() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    let total = 0;

    cart.forEach(item => {
        total += item.price * item.quantity;
    });

    return total;
}
function getTotal() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    let total = 0;

    cart.forEach(item => {
        total += item.price * item.quantity;
    });

    return total;
}
function checkOut(){
  window.location.href = "checkOut.html"
}
// Start with empty text
let output = "";

// Go through each product
for (let i = 0; i < products.length; i++) {
  const item = products[i];
  output += `
    <div class="infobox">
      <img src="${item.src}" alt="gambar elektronik" width= 150 height= 100>
      <h3>${item.name}</h3>
      <p>Price: $${item.price}</p>
      <p>Brand: ${item.brand}</p>
      <button>${item.buy}</button>
    </div>
  `;
}

// Show all products on the page
box.innerHTML = output;
