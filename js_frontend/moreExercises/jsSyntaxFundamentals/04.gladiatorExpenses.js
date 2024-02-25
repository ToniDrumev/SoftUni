function gladiatorExpences(lostFightsCount, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let expenses = 0;

    let helmetRepairCount = Math.floor(lostFightsCount / 2);
    let swordRepairCount = Math.floor(lostFightsCount / 3);
    let shieldRepairCount = Math.floor(lostFightsCount / 6);
    let armorRepairCount = Math.floor(shieldRepairCount / 2);

    expenses += helmetPrice * helmetRepairCount + swordPrice * swordRepairCount + shieldPrice * shieldRepairCount + armorPrice * armorRepairCount;
    
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}
