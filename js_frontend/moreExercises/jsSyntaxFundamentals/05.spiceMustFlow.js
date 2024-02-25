function spiceCount(yield) {
    let days = 0;
    let totalAmount = 0;

    while(yield >= 100){
        totalAmount += yield;
        yield -= 10;
        totalAmount -= 26;
        days += 1;
    }
    if (totalAmount){
        totalAmount -= 26;
    }

    console.log(days);
    console.log(totalAmount);
}
