function solve() {
	const generateFurnitureTextAreaElement = document.querySelector("#exercise textarea:first-of-type");
	const buyFurnitureTextAreaElement = document.querySelector("#exercise textarea:last-of-type");
	const generateFurnitureBtnElement = document.querySelector("#exercise button:first-of-type");
	const buyFurnitureBtnElement = document.querySelector("#exercise button:last-of-type");

	generateFurnitureBtnElement.addEventListener("click", () => {
		let furnitureArray = JSON.parse(generateFurnitureTextAreaElement.value).forEach(furniture => {

			//create table row
			let trElement = document.createElement("tr");

			let imgTdElement = document.createElement("td");
			let imgElement = document.createElement("img");
			imgElement.src = furniture.img;
			imgTdElement.appendChild(imgElement);
			trElement.appendChild(imgTdElement);

			let nameTdElement = document.createElement("td");
			let pNameElement = document.createElement("p");
			pNameElement.textContent = furniture.name;
			nameTdElement.appendChild(pNameElement);
			trElement.appendChild(nameTdElement);

			let priceTdElement = document.createElement("td");
			let pPriceElement = document.createElement("p");
			pPriceElement.textContent = furniture.price;
			priceTdElement.appendChild(pPriceElement);
			trElement.appendChild(priceTdElement);

			let decFactorTdElement = document.createElement("td");
			let pDecFactorElement = document.createElement("p");
			pDecFactorElement.textContent = furniture.decFactor;
			decFactorTdElement.appendChild(pDecFactorElement);
			trElement.appendChild(decFactorTdElement);

			let checkboxTdElement = document.createElement("td");
			let checkboxElement = document.createElement("input");
			checkboxElement.type = "checkbox";
			checkboxTdElement.appendChild(checkboxElement);
			trElement.appendChild(checkboxTdElement);

			document.querySelector("tbody").appendChild(trElement);
		});
	})

	//get and generate furniture
	let furnitureNames = [];
	let totalPrice = 0;
	let totalFactor = 0;

	//mark furniture 
	//buy furniture
	buyFurnitureBtnElement.addEventListener("click", () => {
		const tableCheckboxElements = Array.from(document.querySelectorAll("tbody tr td input[type=checkbox]"));
		for (const checkbox of tableCheckboxElements) {
			if (checkbox.checked) {
				let furnitureRowElement = checkbox.parentElement.parentElement;
				furnitureNames.push(furnitureRowElement.querySelector('td:nth-of-type(2) p').textContent);
				totalPrice += Number(furnitureRowElement.querySelector('td:nth-of-type(3) p').textContent);
				totalFactor += Number(furnitureRowElement.querySelector('td:nth-of-type(4) p').textContent);
			}	
		}

		buyFurnitureTextAreaElement.textContent += `Bought furniture: ${furnitureNames.join(", ")}\n`;
		buyFurnitureTextAreaElement.textContent += `Total price: ${totalPrice.toFixed(2)}\n`;
		buyFurnitureTextAreaElement.textContent += `Average decoration factor: ${totalFactor / furnitureNames.length}`;
	})
}