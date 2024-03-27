function toggle() {
    const buttonElement = document.getElementsByClassName("button")[0];
    const extraElement = document.getElementById("extra");

    let button = buttonElement.textContent;

    if (button === 'More'){
        button = 'Less';
        buttonElement.textContent = button;
        extraElement.style.display = 'block';
    } else {
        button = 'More';
        buttonElement.textContent = button;
        extraElement.style.display = 'none';
    }
}