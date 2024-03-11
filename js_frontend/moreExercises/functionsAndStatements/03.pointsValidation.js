function solve(array) {
    const [x1, y1, x2, y2] = array;

    function checkIsValid(x1, y1, x2, y2) {
        let isValid = false;
        let distance = Math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2));

        if (Number.isInteger(distance)) {
            isValid = true;
        }

        return isValid;
    }

    function printDistance(x1, y1, x2, y2) {
        if (checkIsValid(x1, y1, x2, y2)) {
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
        } else {
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
        }
    }

    printDistance(x1, y1, 0, 0);
    printDistance(x2, y2, 0, 0);
    printDistance(x1, y1, x2, y2);

}
