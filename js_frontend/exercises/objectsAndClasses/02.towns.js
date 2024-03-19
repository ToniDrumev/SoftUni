function solve(array) {
    let towns = []
    for (const line of array) {
        let [town, latitude, longitude] = line.split(' | ');

        console.log({town:town, latitude:parseFloat(latitude).toFixed(2), longitude: parseFloat(longitude).toFixed(2)});
    }
}
