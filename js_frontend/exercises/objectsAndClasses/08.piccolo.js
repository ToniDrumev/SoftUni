function solve(input) {
    const parkingLot = {}

    for (const line of input) {
        const [command, registration] = line.split(', ');

        if (command === 'IN') {
            parkingLot[registration] = registration;
        } else {
            delete parkingLot[registration];
        }
    }

    if (Object.keys(parkingLot).length === 0) {
        console.log("Parking Lot is Empty");
    } else {
        Object.entries(parkingLot)
            .sort((a, b) => a[0].localeCompare(b[0]))
            .forEach(car => console.log(car[0]));
    }
}

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'OUT, CA1234TA']
)