function solve(percent) {
    const printPercent = num => `${num}%`;

    function printLoadingBar(num) {
        return `[${'%'.repeat(num / 10)}${'.'.repeat(10 - num / 10)}]`;
    }

    const printFirstRow = num => `${printPercent(num)} ${printLoadingBar(num)}`;
    
    console.log(printFirstRow(percent));

    if (percent !== 100) {
        console.log('Still loading...');
    } else {
        console.log('Complete!');
    }
}