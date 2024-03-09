function passwordValidator(password) {
    function checkLength(password = '') {
        return password.length >= 6 && password.length <= 10;
    }

    function checkAlphaNumeric(password = '') {
        return password.match(/^[a-zA-Z0-9]+$/g) !== null;
    }

    function checkTwoDigits(password = '') {
        let passAsArray = password.split('');
        let digitCount = 0;

        for (let index = 0; index < passAsArray.length; index++) {
            if (/[\d]/.test(passAsArray[index])) {
                digitCount += 1;
            }
        }

        return digitCount >= 2;
    }

    if (checkLength(password) && checkAlphaNumeric(password) && checkTwoDigits(password)){
        console.log('Password is valid');
    } else {
        if (!checkLength(password)) {
            console.log('Password must be between 6 and 10 characters');
        }

        if (!checkAlphaNumeric(password)) {
            console.log('Password must consist only of letters and digits');
        }

        if (!checkTwoDigits(password)) {
            console.log('Password must have at least 2 digits');
        }
    }
}
