function deleteByEmail() {
    const inputEmailElement = document.querySelector('input[name="email"]');
    const emailsElement = document.querySelectorAll('table#customers tbody tr td:nth-child(2)');
    const resultElement = document.getElementById('result');
    
    for (const email of emailsElement) {
        if (email.textContent === inputEmailElement.value) {
            let row = email.parentNode;
            row.parentElement.removeChild(row);

            resultElement.textContent = 'Deleted.';

            inputEmailElement.value = '';

            return;
        }
    }
    resultElement.textContent = 'Not found.';
}