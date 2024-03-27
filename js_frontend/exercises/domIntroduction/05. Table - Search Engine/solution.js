function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const tableDataElement = document.querySelectorAll('table.container tbody tr');
      const searchInputElement = document.getElementById('searchField');

      const searched = searchInputElement.value;


      for (const tr of tableDataElement) {
         tr.classList.remove('select');
         
         if (tr.textContent.toLowerCase().includes(searched.toLowerCase())) {
            tr.classList.add('select');
         }
      }
      
   }
}