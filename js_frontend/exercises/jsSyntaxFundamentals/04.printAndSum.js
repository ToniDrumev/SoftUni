function printAndSum(num1, num2) {
    let numbers = [];
    let sum = 0;

    for(let i = num1; i <= num2; i++) {
        numbers.push(i);
        sum += i;
    }

    console.log(numbers.join(' '));
    console.log(`Sum: ${sum}`);
}

// printAndSum(5, 10)
// printAndSum(0, 26)
// printAndSum(50, 60)