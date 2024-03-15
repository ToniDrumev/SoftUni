function solve(array) {
    let sortedObject = {};

    // Splitting each string into name and address and populating the object
    array.forEach(item => {
        let [name, address] = item.split(':');
        sortedObject[name] = address;
    });

    // Sorting the object alphabetically by keys (names)
    let sortedKeys = Object.keys(sortedObject).sort();
    let sortedOutput = {};
    sortedKeys.forEach(key => {
        sortedOutput[key] = sortedObject[key];
    });

    // Formatting and displaying the output
    for (let name in sortedOutput) {
        console.log(`${name} -> ${sortedOutput[name]}`);
    }
}
