function solve(array) {
    const employees = {}
    for (const name of array) {
        employees[name] = name.length
    }

    for (const employee in employees) {
        console.log(`Name: ${employee} -- Personal Number: ${employees[employee]}`);
    }
}
