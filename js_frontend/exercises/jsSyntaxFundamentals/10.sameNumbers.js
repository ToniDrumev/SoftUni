function sameNumbers(number) {
    let flag = true;
    let totalSum = 0;
    let lastNumber = number % 10;

    while(number){
        let currentNumber = number % 10;
        number = (number - currentNumber) / 10;
        if (lastNumber != currentNumber) {
            flag = false
        }

        totalSum += currentNumber;

        lastNumber = currentNumber;       
    }

    console.log(flag);
    console.log(totalSum)
}
