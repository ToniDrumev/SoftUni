function calc() {
    const numOne = document.getElementById('num1').value;
    const numTwo = document.getElementById('num2').value;
    const sum = document.getElementById('sum');

    sum.value = Number(numOne) + Number(numTwo);
}
