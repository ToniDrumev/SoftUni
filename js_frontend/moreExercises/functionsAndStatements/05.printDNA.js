function solve(length) {
    const sequence = 'ATCGTTAGGG'.repeat(100000);

    function rowOne(letterOne, letterTwo) {
        console.log(`**${letterOne}${letterTwo}**`);
    }

    function rowTwo(letterOne, letterTwo) {
        console.log(`*${letterOne}--${letterTwo}*`);
    }
    function rowThree(letterOne, letterTwo) {
        console.log(`${letterOne}----${letterTwo}`);
    }
    
    for (let i = 0; i < length * 2; i += 2) {
        let letterOne = sequence.slice(i, i + 1);
        let letterTwo = sequence.slice(i + 1, i + 2)
        
        if ((i / 2) % 4 === 0) {
            rowOne(letterOne, letterTwo);
        } else if ((i / 2) % 4 === 1 || (i / 2) % 4 === 3) {
            rowTwo(letterOne, letterTwo);
        } else {
            rowThree(letterOne, letterTwo);
        }
    }
}
