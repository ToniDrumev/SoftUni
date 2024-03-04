function formatGrade(grade) {
    let gradeText = ''

    if (grade < 3.00) {
        console.log('Fail (2)');
    } else if (grade < 3.50) {
        gradeText = 'Poor';
    } else if (grade < 4.50) {
        gradeText = 'Good';
    } else if (grade < 5.50) {
        gradeText = 'Very good';
    } else {
        gradeText = 'Excellent';
    }
    if (grade >= 3.00) {
        console.log(`${gradeText} (${grade.toFixed(2)})`);
    }
}

formatGrade(3.33)
formatGrade(4.50)
formatGrade(2.99)