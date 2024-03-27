function solve() {
  const inputElement = document.getElementById('input');
  const outputElement = document.getElementById('output');

  let input = inputElement.value.split('.')
    .map(sentence => sentence.trim())
    .filter(sentence => !!sentence); 


  let text = []
  while (input.length > 0) {
    text.push(input.shift());
    if (text.length === 3) {
      outputElement.innerHTML += `<p>${text.join('. ')}.</p>`;
      text = [];
    }
  }

  if (text.length > 0) {
    outputElement.innerHTML += `<p>${text.join('. ')}.</p>`;
  }
}