function solve(text = '') {
    pattern = /#([a-zA-Z]+)/g;
    matches = text.matchAll(pattern);

    for (const match of matches) {
        console.log(match[1]);
    }
}

solve('The symbol # is known #variously in English-speaking #regions as the #number sign')