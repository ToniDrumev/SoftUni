function addItem() {
    const inputElement = document.getElementById('newItemText');
    const itemsElement = document.getElementById('items');

    let text = inputElement.value;
    let li = document.createElement('li');
    let deleteItem = document.createElement('a');

    deleteItem.textContent = '[Delete]'
    deleteItem.href = '#'

    li.appendChild(document.createTextNode(text));
    itemsElement.appendChild(li);
    li.appendChild(deleteItem);
    inputElement.value = '';

    deleteItem.addEventListener('click', deleteFunc => {
        li.remove();
    });
}