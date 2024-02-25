function uppercaseWords(str) {
    let arr = str.match(/\w+/g);
    let arr2 = [];

    for (let i = 0; i < arr.length; i++) {
        arr2.push(arr[i].toUpperCase());
    }

    console.log(arr2.join(', '))
}