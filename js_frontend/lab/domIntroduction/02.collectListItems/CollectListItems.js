function extractText() {
    const listItems = document.querySelectorAll("ul#items li");
    const textArea = document.getElementById("result");

    for (const list of listItems) {
        textArea.value += list.textContent + '\n';
    }

}