function simpleCalculator(a, op, b) {
    let result = 0;

    switch(op){
        case '+':
            result = a + b;
            break;
        case '-':
            result = a - b;
            break;
        case '*':
            result = a * b;
            break;
        case '/':
            result = a / b;
            break;
        case '%':
            result = a % b;
            break;
    }

    console.log(result.toFixed(2));
}
