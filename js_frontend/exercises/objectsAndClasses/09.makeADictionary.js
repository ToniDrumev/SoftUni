function solve(input) {
    let dictionary = {}
    for (const line of input) {
        const word = JSON.parse(line);
        Object.assign(dictionary, word)
    }

    Object.entries(dictionary)
        .sort((a, b) => a[0].localeCompare(b[0]))
        .forEach(term => console.log(`Term: ${term[0]} => Definition: ${term[1]}`));
}