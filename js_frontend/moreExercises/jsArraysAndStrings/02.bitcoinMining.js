function solve(shiftGrams = []) {
    let dailyQuantity = 0;
    let goldQuantity = 0;
    let bitcoinQuantity = 0;
    let firstBitcoinPurchasedDay = 0;
    let pricePerGram = 67.51;
    let pricePerBitcoin = 11949.16;


    for (let i = 0; i < shiftGrams.length; i++) {
        dailyQuantity = shiftGrams[i];

        if ((i + 1) % 3 === 0) {
            dailyQuantity = 0.7 * dailyQuantity;
        }

        goldQuantity += dailyQuantity * pricePerGram;

        while((goldQuantity - pricePerBitcoin) >= 0){
            goldQuantity -= pricePerBitcoin;
            bitcoinQuantity += 1;

            if (bitcoinQuantity === 1){
                firstBitcoinPurchasedDay = i + 1;
            }
        }
    }

    console.log(`Bought bitcoins: ${bitcoinQuantity}`);
    if (firstBitcoinPurchasedDay){
        console.log(`Day of the first purchased bitcoin: ${firstBitcoinPurchasedDay}`);
    }
    console.log(`Left money: ${goldQuantity.toFixed(2)} lv.`);
}

solve([50, 100])