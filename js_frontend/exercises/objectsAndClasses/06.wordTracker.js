function solve(words) {
    let searchedWords = words.shift().split(' ');
    let searchedWordCounter = {};

    for (const word of searchedWords) {
        searchedWordCounter[word] = 0;
    }

    for (const word of words) {
        if (searchedWords.includes(word)) {
            searchedWordCounter[word] += 1;
        }
    }

    Object.entries(searchedWordCounter)
        .sort((a, b) => b[1] - a[1])
        .forEach((word) => console.log(`${word[0]} - ${word[1]}`));
}
