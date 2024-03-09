function solve(number) {
    function getPositiveDivisors(num) {
        const divisors = []
        for (let i = 1; i < num; i++) {
            if (num % i === 0) {
                divisors.push(i);
            }
        }

        return divisors;
    }

    const sumDivisors = divisors => getPositiveDivisors(divisors).reduce((a, b) => a + b, 0);
    
    if (sumDivisors(number) === number) {
        console.log('We have a perfect number!');
    } else {
        console.log('It\'s not so perfect.');
    }
}
