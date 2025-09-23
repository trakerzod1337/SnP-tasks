import re


def is_palindrome(string):
    if not isinstance(string, (str, int, float)):
        return False

    if isinstance(string, (int, float)):
        string = str(string)

    cleaned_string = re.sub(r'[^a-zа-яё0-9]', '', string.lower())

    if not cleaned_string:
        return False

    return cleaned_string == cleaned_string[::-1]

#Тестирование
print(is_palindrome("A man, a plan, a canal -- Panama"))  # True
print(is_palindrome("Madam, I'm Adam!"))                 # True
print(is_palindrome(333))                                # True
print(is_palindrome(None))                               # False
print(is_palindrome("Abracadabra")) # False
print(is_palindrome(33.3))