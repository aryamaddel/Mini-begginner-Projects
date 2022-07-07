def armstrong_number(number):
    """
    Function to check if a number is an Armstrong number
    """
    if number < 0:
        return False
    else:
        number_str = str(number)
        sum = 0
        for digit in number_str:
            sum += int(digit)**3
            print(int(digit)**3)
        if sum == number:
            return True
        else:
            return False

number = int(input("Enter a number: "))
print(armstrong_number(number))