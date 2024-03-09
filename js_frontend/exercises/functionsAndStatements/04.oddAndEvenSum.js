function oddAndEvenSum(number) {
    let evenSum = 0;
    let oddSum = 0;
    const numLength = number.toString().length;

    for (let i = 1; i <= numLength; i++) {
        let currentNum = number % 10;
        number -= currentNum;

        if (currentNum % 2 === 0){
            evenSum += currentNum;
        } else {
            oddSum += currentNum;
        }

        number /= 10;
    }

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}
