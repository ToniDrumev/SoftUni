function create(words) {
   const contentElement = document.getElementById("content");

   for (const word of words) {      
      let pElement = document.createElement("p");
      pElement.textContent = word;
      pElement.style.display = "none";
      
      let divElement = document.createElement("div");
      divElement.appendChild(pElement);
      divElement.addEventListener("click", function show() {
         pElement.style.display = "block";
      });

      contentElement.appendChild(divElement);
   };
}

