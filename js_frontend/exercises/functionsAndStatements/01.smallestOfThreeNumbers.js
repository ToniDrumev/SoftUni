function smallestOfThreeNumbers(numOne, numTwo, numThree) {
    if (numOne <= numTwo && numOne <= numThree) {
        return numOne;
    } else if (numThree <= numOne) {
        if (numThree <= numTwo){
            return numThree
        } else {
            return numTwo;
        }
    } else {
        return numTwo;
    }
}