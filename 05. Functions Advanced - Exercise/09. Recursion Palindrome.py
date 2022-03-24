def palindrome(word, ind):
    if ind == len(word) // 2:
        return f"{word} is a palindrome"
    left = word[ind]
    right = word[len(word) -1 -ind]

    if left != right:
        return f"{word} is not a palindrome"

    return palindrome(word, ind + 1)

print(palindrome("abcba", 0))