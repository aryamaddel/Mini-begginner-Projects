def palindrome(value):
    reversed_value = ''
    for reverse_element in reversed(value):
        reversed_value += reverse_element
    if reversed_value == value:
        return True
    else:
        return False

value = input('Enter a value: ')
print(palindrome(value))