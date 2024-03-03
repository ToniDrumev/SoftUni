function solve(arr, number) {
    for(let i = 0; i < number; i++){
        let currItem = arr.shift()
        arr.push(currItem)
    }

    console.log(arr.join(' '));
}
