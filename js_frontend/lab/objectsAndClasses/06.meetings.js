function solve(meetingsArray = []) {
    let meetings = {}

    for (const meeting of meetingsArray) {
        let [weekday, person] = meeting.split(' ');
        
        if (!meetings[weekday]){
            meetings[weekday] = person;
            console.log(`Scheduled for ${weekday}`);
        } else {
            console.log(`Conflict on ${weekday}!`);
        }
    }

    for (const weekday in meetings) {
        console.log(`${weekday} -> ${meetings[weekday]}`);
    }
}
