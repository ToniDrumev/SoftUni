function search() {
   const townsElement = document.querySelectorAll("ul#towns li");
   const searchTextElement = document.getElementById("searchText");
   const resultElement = document.getElementById("result");

   let townsArray = Array.from(townsElement);
   let searchText = searchTextElement.value;
   let result = resultElement.textContent;

   let counter = 0;
   for (const town of townsArray) {
      if (town.textContent.toLowerCase().includes(searchText.toLowerCase())){
         town.style.fontWeight = 'bold';
         town.style.textDecoration = 'underline';

         counter += 1;
      }
   }

   result = `${counter} matches found`;
   resultElement.textContent = result;
}
