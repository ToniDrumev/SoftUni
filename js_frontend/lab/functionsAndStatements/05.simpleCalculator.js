function simpleCalculator(numOne, numTwo, operator) {
    switch (operator) {
        case 'multiply':
            return numOne * numTwo;
        case 'divide':
            return numOne / numTwo;
        case 'add':
            return numOne + numTwo;
        case 'subtract':
            return numOne - numTwo;
    }
}
