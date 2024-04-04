function addItem() {
    const dropDownMenuElement = document.getElementById("menu");
    const newItemTextElement = document.getElementById("newItemText");
    const newItemValueElement = document.getElementById("newItemValue");

    let optionElement = document.createElement("option");
    optionElement.textContent = newItemTextElement.value;
    optionElement.value = newItemValueElement.value;
    dropDownMenuElement.appendChild(optionElement);

    newItemTextElement.value = '';
    newItemValueElement.value = '';
}