function charactersInRange(first, second) {
    const asciiCharsRange = [];
    asciiCharsRange.push(first.charCodeAt());
    asciiCharsRange.push(second.charCodeAt());
    asciiCharsRange.sort((a, b) => a - b);

    let characters = []

    for (let i = asciiCharsRange[0]; i < asciiCharsRange[1] - 1; i++) {
        characters.push(String.fromCharCode(i + 1));
    }

    return characters.join(' ');
}