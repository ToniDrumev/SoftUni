function solve(array) {
    const username = array[0];
    for (let i = 1; i < array.length; i++) {
        let currentPasswordAsArr = array[i].split('');
        let currentReversedPassword = currentPasswordAsArr.reverse().join('');
       
        if (i === 4) {
            if (currentReversedPassword === username){
                console.log(`User ${username} logged in.`);
                break;
            } else {
                console.log(`User ${username} blocked!`);
            }
        } else {
            if (currentReversedPassword === username){
                console.log(`User ${username} logged in.`);
                break;
            } else {
                console.log('Incorrect password. Try again.');
            }
        }
    }
}
