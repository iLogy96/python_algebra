def isPalindrome(word):
    if word.lower()==word[::-1].lower():
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is NOT a palindrome")


isPalindrome("Anavolimilovana")
isPalindrome("volimilovana")
