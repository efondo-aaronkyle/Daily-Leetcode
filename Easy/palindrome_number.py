def is_palindrome(number):
    original_number, reverse_number = number, 0 

    if number < 0:
        return False

    while number > 0:
        reverse_number = reverse_number * 10 + number % 10
        number //= 10
    return original_number == reverse_number

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))