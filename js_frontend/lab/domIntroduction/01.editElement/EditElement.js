function editElement(reference, match, replacer) {
    const content = reference.textContent;
    const matcher = new RegExp(match, 'g');
    const editedContent = content.replace(matcher, replacer);
    reference.textContent = editedContent;
}