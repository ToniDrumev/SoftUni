function ages(num) {
    let age;

    if (num >= 0 && num <= 2) {
        age = 'baby';
    } else if (num >= 3 && num <= 13) {
        age = 'child';
    } else if (num >= 14 && num <= 19) {
        age = 'teenager';
    } else if (num >= 20 && num <= 65) {
        age = 'adult';
    } else if (num >= 66) {
        age = 'elder';
    } else {
        age = 'out of bounds';
    }

    console.log(age);
}
