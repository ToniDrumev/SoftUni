function solve(string) {
    let matches = string.matchAll(/[A-Z][a-z]*/g);
    const result = [];

    for (const match of matches) {
        result.push(match[0]);
    }

    console.log(result.join(', '));
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan')