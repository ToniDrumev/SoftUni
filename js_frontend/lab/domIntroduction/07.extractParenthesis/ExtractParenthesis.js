function extract(content) {
    const contentElement = document.getElementById('content').textContent;
    const matcher = /\((.*?)\)/g;
    let matches = [...contentElement.matchAll(matcher)];

    let extractedContents = matches.map(match => match[1]);
    // console.log(extractedContents.join('\n'));
    return extractedContents.join('\n');
}