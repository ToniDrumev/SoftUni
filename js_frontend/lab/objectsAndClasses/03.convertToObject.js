function solve(jsonStr) {
    const city = JSON.parse(jsonStr)

    for (const key in city) {
        console.log(`${key}: ${city[key]}`);
    }
}
