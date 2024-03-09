function solve(numberOne, numberTwo) {
    function factorialDivision(num) {
        if (num <= 1){
            return 1;
        }

        return num *= factorialDivision(num - 1);
    }

    let reslt = factorialDivision(numberOne) / factorialDivision(numberTwo);

    console.log(reslt.toFixed(2));
}