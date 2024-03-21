function sumTable() {
    let priceOfProductsElements = document.querySelectorAll('table td:nth-of-type(2n)');
    const sumElement = document.getElementById('sum');
    let result = 0;
    for (let i = 0; i < priceOfProductsElements.length - 1; i++ ) {
        result += Number(priceOfProductsElements[i].textContent);
    }

    sumElement.textContent = result;
}