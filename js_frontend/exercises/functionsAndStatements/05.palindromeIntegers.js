function palindromeIntegers(numbers) {
    let numberAsText = '';
    function reversedNumberAsText(num = '') {
        reversedNumber = num.split('').reverse().join('');
        return reversedNumber;
    }

    for (const number of numbers) {
        numberAsText = number.toString();
        let reversedNumber = reversedNumberAsText(numberAsText);

        if (numberAsText === reversedNumber){
            console.log(true);
        } else {
            console.log(false);
        }
    }
}
