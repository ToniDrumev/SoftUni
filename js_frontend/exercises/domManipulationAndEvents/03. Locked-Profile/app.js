function lockedProfile() {
    const profileElements = document.querySelectorAll(".profile");


    for (const profile of profileElements) {
        const showHideButton = profile.querySelector('button');
        const lockButtonElement = profile.querySelector("input[type=radio][value=lock]")

        showHideButton.addEventListener("click", (e) => {
            if (lockButtonElement.checked) {
                return;
            }

            let additionInformationElement = showHideButton.previousElementSibling;

            if (showHideButton.textContent === 'Show more') {
                additionInformationElement.style.display = 'block';
                showHideButton.textContent = 'Hide it';
            } else {
                additionInformationElement.style.display = 'none';
                showHideButton.textContent = 'Show more';
            }
        })
    }
}
