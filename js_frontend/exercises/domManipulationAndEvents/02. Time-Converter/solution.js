function attachEventsListeners() {
    const dayTextElement = document.getElementById("days");
    const hourTextElement = document.getElementById("hours");
    const minuteTextElement = document.getElementById("minutes");
    const secondTextElement = document.getElementById("seconds");

    const dayButtonElement = document.getElementById("daysBtn");
    const hourButtonElement = document.getElementById("hoursBtn");
    const minuteButtonElement = document.getElementById("minutesBtn");
    const secondButtonElement = document.getElementById("secondsBtn");

    function dayConverter() {
        const daysValue = Number(dayTextElement.value);
        hourTextElement.value = daysValue * 24;
        minuteTextElement.value = daysValue * 24 * 60;
        secondTextElement.value = daysValue * 24 * 60 * 60;
    }
    function hourConverter() {
        const hourValue = Number(hourTextElement.value);
        dayTextElement.value = hourValue / 24;
        minuteTextElement.value = hourValue * 60;
        secondTextElement.value = hourValue * 60 * 60;
    }
    function minuteConverter() {
        const minuteValue = Number(minuteTextElement.value);
        dayTextElement.value = minuteValue / (24 * 60);
        hourTextElement.value = minuteValue / 60;
        secondTextElement.value = minuteValue * 60;
    }
    function secondConverter() {
        const secondValue = Number(secondTextElement.value);
        dayTextElement.value = secondValue / (24 * 60 * 60);
        hourTextElement.value = secondValue / (60 * 60);
        minuteTextElement.value = secondValue / 60;
    }

    dayButtonElement.addEventListener("click", dayConverter);
    hourButtonElement.addEventListener("click", hourConverter);
    minuteButtonElement.addEventListener("click", minuteConverter);
    secondButtonElement.addEventListener("click", secondConverter);    
}

