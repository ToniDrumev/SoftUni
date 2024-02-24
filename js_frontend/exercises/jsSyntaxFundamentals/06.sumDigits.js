function sumDigits(num) {
    let sum = 0;

    while(num){
        sum += num % 10;
        num -= num %10;
        num /= 10
    }

    console.log(sum);
}