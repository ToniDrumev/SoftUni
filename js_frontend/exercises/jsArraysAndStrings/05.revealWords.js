function solve(words, text = '') {
    wordsAsArray = words.split(', ');
    const matches = text.matchAll(/\*+/g);

    for (const match of matches) {
        let word = wordsAsArray.find(w => w.length === match[0].length);

        text = text.replace(match[0], word)
    }

    console.log(text);
}



solve('great, learning',
    'softuni is ***** place for ******** new programming languages *****'
)