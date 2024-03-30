function attachGradientEvents() {
    const hoverElement = document.getElementById('gradient');
    const resultElement = document.getElementById('result');

    hoverElement.addEventListener('mousemove', function hoverMouse(event) {
        let horizontalOffset = event.offsetX / (event.target.clientWidth - 1);
        resultElement.textContent = `${Math.floor(horizontalOffset * 100)}%`;
    });

    hoverElement.addEventListener('mouseout', function outMouse() {
        resultElement.textContent = '';
    })
}