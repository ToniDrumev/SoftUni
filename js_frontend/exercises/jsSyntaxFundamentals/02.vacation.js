function vacationPrice(peopleCount, typeOfGroup, dayOfWeek) {
    let totalPrice = 0;
    let pricePerPerson = 0;

    switch(typeOfGroup) {
        case 'Students':
            switch(dayOfWeek) {
                case 'Friday':
                    pricePerPerson = 8.45;
                    break;
                case 'Saturday':
                    pricePerPerson = 9.80;
                    break;
                case 'Sunday':
                    pricePerPerson = 10.46;
                    break;
            }
            break;
        case 'Business':
            switch(dayOfWeek) {
                case 'Friday':
                    pricePerPerson = 10.90;
                    break;
                case 'Saturday':
                    pricePerPerson = 15.60;
                    break;
                case 'Sunday':
                    pricePerPerson = 16;
                    break;
            }
            break;
        case 'Regular':
            switch(dayOfWeek) {
                case 'Friday':
                    pricePerPerson = 15;
                    break;
                case 'Saturday':
                    pricePerPerson = 20;
                    break;
                case 'Sunday':
                    pricePerPerson = 22.50;
                    break;
            }
            break;
    }

    switch (typeOfGroup) {
        case 'Students':
            totalPrice = peopleCount * pricePerPerson;
            if (peopleCount >= 30){
                totalPrice *= 0.85;
            }
            
            break;
        case 'Business':
            if (peopleCount >= 100) {
                peopleCount -= 10;
            }

            totalPrice = peopleCount * pricePerPerson;
            break;

        case 'Regular':
            totalPrice = peopleCount * pricePerPerson;

            if (peopleCount >= 10 && peopleCount <=20) {
                totalPrice *= 0.95;
            }
            break;
    }

    if (peopleCount <= 0) {
        totalPrice = 0;
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}
