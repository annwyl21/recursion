def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True

    # Check if the first and last characters are the same
    if s[0] == s[-1]:
        # Recursive call excluding the first and last characters
        return is_palindrome(s[1:-1])

    # If the first and last characters don't match, it's not a palindrome
    return False

# Test the function
print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False
