function solve() {
  const inputElement = document.getElementById('text');
  const namingConventionElement = document.getElementById('naming-convention');

  const resultElement = document.querySelector('#result');

  const text = inputElement.value;
  const namingConvention = namingConventionElement.value;

  let inputElementArray = text.toLowerCase().split(' ');

  let result = [];

  if (namingConvention === 'Pascal Case') {
    for (const word of inputElementArray) {
      const modifiedWord = word.charAt(0).toUpperCase() + word.slice(1);

      result.push(modifiedWord);
    }

    resultElement.textContent = result.join('');
  } else if (namingConvention === 'Camel Case') {
    result.push(inputElementArray[0]);

    for (let i = 1; i < inputElementArray.length; i++) {
      const modifiedWord = inputElementArray[i].charAt(0).toUpperCase() + inputElementArray[i].slice(1);

      result.push(modifiedWord);
    }

    resultElement.textContent = result.join('');
  } else {
    resultElement.textContent = 'Error!'
  }
}