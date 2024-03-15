function solve(array = []) {
    let phoneBook = {}
    for (const line of array) {
        let [key, value] = line.split(' ');

        phoneBook[key] = value;
    }

    for (const person in phoneBook) {
        console.log(`${person} -> ${phoneBook[person]}`);
    }
}
