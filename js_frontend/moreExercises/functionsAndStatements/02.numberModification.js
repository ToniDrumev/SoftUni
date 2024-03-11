function solve(number) {
    function checkAvgDigit(num = 0) {
        let numAsArray = Array.from(num.toString(), num => Number(num));
        let sumOfArray = numAsArray.reduce((a, b) => a + b, 0);

        if (sumOfArray / numAsArray.length >= 5) {
            return true;
        }

        return false;
    }

    function numberModification(num) {
        while (!checkAvgDigit(num)) {
            num *= 10;
            num += 9;
        }

        return num;
    }

    console.log(numberModification(number));
}
