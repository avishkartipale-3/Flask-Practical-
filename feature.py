def check_palindrome(text):
    text = text.replace(" ", "").lower()
    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    else:
        return False


word = input("Enter a word or sentence: ")

if check_palindrome(word):
    print("It is a palindrome! ✅")
else:
    print("It is not a palindrome word. ❌")

