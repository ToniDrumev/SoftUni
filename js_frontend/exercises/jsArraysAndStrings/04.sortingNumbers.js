function solve(numbers) {
    let result = [];
    let sortedNumbers = numbers.slice().sort((a, b) => a - b);

    for (let i = 0; i < numbers.length; i++) {
        if (i % 2 == 0) {
            result.push(sortedNumbers.shift())
        } else {
            result.push(sortedNumbers.pop())
        }
    }

    return result;
}

