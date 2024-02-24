function cookWithNumbers(numAsStr, operation1, operation2, operation3, operation4, operation5) {
    let number = parseInt(numAsStr);
    let operations = [operation1, operation2, operation3, operation4, operation5]

    for (let i = 1; i <=5; i++) {
        let operation = operations[i - 1];

        switch(operation) {
            case 'chop':
                number /= 2;
                break;
            case 'dice':
                number = Math.sqrt(number);
                break;
            case 'spice':
                number += 1;
                break;
            case 'bake':
                number *= 3;
                break;
            case 'fillet':
                number -= 0.20 * number;
                break;
        }

        console.log(number);
    }
}
