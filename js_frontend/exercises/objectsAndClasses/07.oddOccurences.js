function solve(input) {
    const words = input.toLowerCase().split(' ')
    let wordsCounter = {}

    for (const word of words) {
        if (!wordsCounter[word]) {
            wordsCounter[word] = 0;
        }

        wordsCounter[word] += 1
    }

    let result = []

    Object.entries(wordsCounter)
        .filter(word => word[1] % 2 != 0)
        .forEach(word => result.push(word[0]));

    console.log(result.join(' '));
}
