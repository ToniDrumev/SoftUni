function theatrePromotions(typeOfDay, age) {
    let priceOfTicket;
    if (0 <= age && age <= 18) {
            switch(typeOfDay) {
                case 'Weekday': priceOfTicket = '12$';
                break;
                case 'Weekend': priceOfTicket = '15$';
                break;
                case 'Holiday': priceOfTicket = '5$';
                break;
            }
        } else if(18 <= age && age <= 64) {
            switch(typeOfDay) {
                case 'Weekday': priceOfTicket = '18$';
                break;
                case 'Weekend': priceOfTicket = '20$';
                break;
                case 'Holiday': priceOfTicket = '12$';
                break;
            }
        } else if (64 <= age && age <= 122) {
            switch(typeOfDay) {
                case 'Weekday': priceOfTicket = '12$';
                break;
                case 'Weekend': priceOfTicket = '15$';
                break;
                case 'Holiday': priceOfTicket = '10$';
                break;
            }
        } else {
            priceOfTicket = 'Error!'
        }
    
    console.log(priceOfTicket)
}
