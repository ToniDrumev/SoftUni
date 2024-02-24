function speedChecker(speed, drivingArea) {
    let speedLimit = 0;

    switch(drivingArea) {
        case 'motorway':
            speedLimit = 130;
            break;
        case 'interstate':
            speedLimit = 90;
            break;
        case 'city':
            speedLimit = 50;
            break;
        case 'residential':
            speedLimit = 20;
            break;
    }

    speedDifference = speed - speedLimit;

    if (speedDifference <= 0) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`)
    } else {
        let status;

        if (speedDifference <= 20) {
            status = 'speeding'
        } else if (speedDifference <= 40) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }

        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
    }
}
