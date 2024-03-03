function solve(word, text) {
    let textAsArray = text.split(' ');
    let foundWord = false;

    for (const wordInText of textAsArray) {
        if (wordInText.toLowerCase() === word.toLowerCase()){
            console.log(word);
            foundWord = true;
            break;
        }
    }

    if (!foundWord){
        console.log(`${word} not found!`);
    }
}

solve('python',
'JavaScript is the best programming language'
)