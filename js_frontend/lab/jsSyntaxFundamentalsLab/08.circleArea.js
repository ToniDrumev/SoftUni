function circleArea(param) {
    if (typeof(param) == 'number')
        console.log((Math.PI * (param ** 2)).toFixed(2))
    else
        console.log(`We can not calculate the circle area, because we receive a ${typeof(param)}.`)
    }
