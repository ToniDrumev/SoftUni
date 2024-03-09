function solve(number) {
    function matrixRow(num=0) {
        const row = []
        for (let i = 1; i <= num; i++){
            row.push(num)
        }

        console.log(row.join(' '));
    }

    function printMatrix(num) {
        for (let index = 1; index <= num; index++) {
            matrixRow(num)
        }
    }

    printMatrix(number);
}