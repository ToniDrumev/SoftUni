function colorize() {
    let evenRow = document.querySelectorAll('tr:nth-of-type(even)');
    for (const row of evenRow) {
        row.style.backgroundColor = "teal";
    }
}