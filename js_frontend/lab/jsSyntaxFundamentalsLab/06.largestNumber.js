function largestNumber(number1, number2, number3) {
    let largestNumber;

    if (number1 > number2 && number1 > number3)
        largestNumber = number1;
    else if (number2 > number1 && number2 > number3)
        largestNumber = number2;
    else
        largestNumber = number3;

    console.log(`The largest number is ${largestNumber}.`)
}
