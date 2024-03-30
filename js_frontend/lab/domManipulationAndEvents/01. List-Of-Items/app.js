function addItem() {
    const inputTextElement = document.getElementById('newItemText');
    const ulItemsElement = document.getElementById('items');
    
    let text = inputTextElement.value;
    let li = document.createElement('li');

    li.appendChild(document.createTextNode(text));
    ulItemsElement.appendChild(li);

    //Clear input
    inputTextElement.value = '';
}
