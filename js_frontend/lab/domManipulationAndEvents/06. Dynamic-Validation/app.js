function validate() {
    const inputElement = document.getElementById("email");

    inputElement.addEventListener("change", function (event) {
        const inputValue = event.target.value;
        const validRegex = /[a-z]+@[a-z]+\.[a-z]+/;

        if (!validRegex.test(inputValue)) {
            inputElement.classList.add("error");
        } else {
            inputElement.classList.remove("error");
        }
    })
}