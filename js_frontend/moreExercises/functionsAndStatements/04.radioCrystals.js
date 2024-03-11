function solve(array) {
    const target = array[0];

    function cut(amount, target) {
        let counter = 0;
        while (amount / 4 >= target) {
            counter += 1;
            amount /= 4;
        }
        console.log(`Cut x${counter}`);
        return amount;
    }

    function lap(amount, target) {
        let counter = 0;
        while (amount * 0.8 >= target) {
            counter += 1;
            amount = amount - 0.2 * amount;
        }
        console.log(`Lap x${counter}`);

        return amount;
    }

    function grind(amount, target) {
        let counter = 0;
        while (amount - 20 >= target) {
            counter += 1;
            amount -= 20;
        }
        console.log(`Grind x${counter}`);

        return amount;
    }

    function etch(amount, target) {
        let counter = 0;
        while (amount - 2 >= target - 1) {
            counter += 1;
            amount -= 2;
        }
        console.log(`Etch x${counter}`);

        return amount;
    }

    function xRay(amount) {
        console.log('X-ray x1');
        return amount += 1;
    }

    function transportingAndWashing(amount) {
        console.log('Transporting and washing');
        return Math.floor(amount);
    }

    for (let index = 1; index < array.length; index++) {
        let amount = array[index];
        console.log(`Processing chunk ${amount} microns`);

        while (amount !== target) {
            if (amount / 4 >= target) {
                amount = cut(amount, target);
                amount = transportingAndWashing(amount);
            } else if (amount * 0.8 >= target) {
                amount = lap(amount, target);
                amount = transportingAndWashing(amount);
            } else if (amount - 20 >= target) {
                amount = grind(amount, target);
                amount = transportingAndWashing(amount);
            } else if (amount - 2 >= target) {
                amount = etch(amount, target);
                amount = transportingAndWashing(amount);
            } else {
                amount = xRay(amount);
            }
        }
        console.log(`Finished crystal ${target} microns`);
    }
}
