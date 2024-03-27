function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {
      const inputElement = document.querySelector('div#inputs textarea');
      const bestRestaurantElement = document.querySelector('#bestRestaurant p');
      const workersElement = document.querySelector('#workers p');

      let inputArray = JSON.parse(inputElement.value);

      let bestRestaurant;
      let restaurants = {};

      for (const restaurant of inputArray) {
         let [name, workers] = restaurant.split(' - ');

         if (!Object.keys(restaurants).includes(name)) {
            restaurants[name] = {
               'workers': [],
               'averageSalary': 0,
               'bestSalary': 0,
            }
         }

         let currentWorkers = workers
            .split(', ')
            .map(worker => worker.split(' '))
            .sort((a, b) => Number(b[1]) - Number(a[1]));

         restaurants[name].workers.push(...currentWorkers);
         restaurants[name].workers.sort((a, b) => b[1] - a[1]);
      }

      for (const restaurant in restaurants) {
         let totalSum = restaurants[restaurant].workers.reduce((totalSum, worker) => totalSum + Number(worker[1]), 0);
         restaurants[restaurant].averageSalary = totalSum / restaurants[restaurant].workers.length;

         restaurants[restaurant].bestSalary = restaurants[restaurant].workers[0][1];
      }

      bestRestaurant = Object.keys(restaurants).reduce((best, restaurant) => {
         return restaurants[restaurant].averageSalary > restaurants[best].averageSalary ? restaurant : best;
     });

     bestRestaurantElement.textContent = `Name: ${bestRestaurant} Average Salary: ${restaurants[bestRestaurant].averageSalary.toFixed(2)} Best Salary: ${Number(restaurants[bestRestaurant].bestSalary).toFixed(2)}`;

     let workersText = "";
     for (const worker of restaurants[bestRestaurant].workers) {
      workersText += `Name: ${worker[0]} With Salary: ${Number(worker[1])} `;
     }

     workersElement.textContent = workersText.trim();
   }
}