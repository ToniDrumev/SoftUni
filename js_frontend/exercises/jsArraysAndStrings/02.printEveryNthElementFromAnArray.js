function solve(arr, number) {
    let nthElemArr = []
    for(let i = 0; i < arr.length; i += number){
        nthElemArr.push(arr[i]);
    }

    return nthElemArr;
}
