function signChecker(numOne, numTwo, numThree) {
    function checkSign(num) {
        if (num > 0) {
            return true;
        }

        return false;
    }

    if (checkSign(numOne) && checkSign(numTwo)) {
        if (checkSign(numThree)) {
            return 'Positive';
        } else {
            return 'Negative';
        }
    } else if (!checkSign(numOne) && !checkSign(numTwo)) {
        if (checkSign(numThree)) {
            return 'Positive';
        } else {
            return 'Negative';
        }
    } else {
        if (checkSign(numThree)) {
            return 'Negative';
        } else {
            return 'Positive';
        }
    }
}

console.log(signChecker(-1,
    -2,
    -3
   ));