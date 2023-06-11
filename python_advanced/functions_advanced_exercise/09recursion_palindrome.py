def palindrome(word, index):
    if word[index] != word[- index - 1]:
        return f"{word} is not a palindrome"

    if len(word) // 2 == index:
        return f"{word} is a palindrome"

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))