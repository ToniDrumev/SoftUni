function mathOperations(number1, number2, operator) {
    let result;

    switch(operator){
        case '+': result = number1 + number2; 
        break;
    }
    switch(operator){
        case '-': result = number1 - number2; 
        break;
    }
    switch(operator){
        case '*': result = number1 * number2; 
        break;
    }
    switch(operator){
        case '/': result = number1 / number2; 
        break;
    }
    switch(operator){
        case '%': result = number1 % number2; 
        break;
    }
    switch(operator){
        case '**': result = number1 ** number2; 
        break;
    }

    console.log(result)
}
