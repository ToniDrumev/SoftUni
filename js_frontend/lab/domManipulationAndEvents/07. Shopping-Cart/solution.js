function solve() {
   const productsElement = document.querySelectorAll(".product");
   const textareaElement = document.getElementsByTagName("textarea")[0];
   const chceckoutButtonElement = document.querySelector(".checkout");

   const products = {};

   function add() {
      let product = this.parentNode.parentNode;
      let name = product.querySelector(".product-title").textContent;
      let price = Number(product.querySelector(".product-line-price").textContent);

      textareaElement.textContent += `Added ${name} for ${price.toFixed(2)} to the cart.\n`;

      if (!Object.keys(products).includes(name)) {
         products[name] = 0;
      }

      products[name] += price;
   }

   Array
      .from(productsElement)
      .forEach(product => product.querySelector("button.add-product").addEventListener("click", add));

   chceckoutButtonElement.addEventListener("click", function checkout() {
      const totalPrice = Array.from(Object.values(products)).reduce((acc, price) => acc + price, 0);
      const productNames = Object.keys(products).join(", ");

      textareaElement.textContent += `You bought ${productNames} for ${totalPrice.toFixed(2)}.`;

      chceckoutButtonElement.removeEventListener("click", checkout);
      Array
      .from(productsElement)
      .forEach(product => product.querySelector("button.add-product").removeEventListener("click", add));

   });
}