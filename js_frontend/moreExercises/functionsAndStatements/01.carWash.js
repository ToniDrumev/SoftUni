function solve(commands) {
    const soap = num => num + 10;
    const water = num => num += 0.2 * num;
    const vacuumCleaner = num => num += 0.25 * num;
    const mud = num => num -= 0.1 * num;

    let clean = 0;

    for (const command of commands) {
        switch (command){
            case 'soap':
                clean = soap(clean);
                break;
            case 'water':
                clean = water(clean);
                break;
            case 'vacuum cleaner':
                clean = vacuumCleaner(clean);
                break;
            case 'mud':
                clean = mud(clean);
                break;
        }
    }

    console.log(`The car is ${clean.toFixed(2)}% clean.`);
}
