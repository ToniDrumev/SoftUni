function encodeAndDecodeMessages() {
    const getMessageTextAreaElement = document.querySelector("main div:first-of-type textarea");
    const getMessageBtnElement = document.querySelector("main div:first-of-type button");
    const outputMessageTextAreaElement = document.querySelector("main div:last-of-type textarea");
    const decodeBtnElement = document.querySelector("main div:last-of-type button");

    function encode(e) {
        let messageToEncode = getMessageTextAreaElement.value;
        let encodedMessage = Array
            .from(messageToEncode)
            .map(ch => {
                return String.fromCharCode(ch.charCodeAt(0) + 1);
            })
            .join("");

        outputMessageTextAreaElement.value = encodedMessage;
        getMessageTextAreaElement.value = '';
    }

    function decode(e) {
        let messageToDecode = outputMessageTextAreaElement.value;
        let decodedMessage = Array
            .from(messageToDecode)
            .map(ch => {
                return String.fromCharCode(ch.charCodeAt(0) - 1);
            })
            .join("");

        outputMessageTextAreaElement.value = decodedMessage;
    }

    getMessageBtnElement.addEventListener("click", encode);
    decodeBtnElement.addEventListener("click", decode);
}