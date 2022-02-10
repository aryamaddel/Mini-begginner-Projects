list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # sorted list

# numbner to search
number = int(input('Enter your element to be searched\n:'))


def search(list, n):
    for index, element in enumerate(list):
        if element == n:
            return index
    return False


search_result = search(list, number)
if search_result != False:
    print('Element found at : ', search_result)
elif search_result == False:
    print("Element NOT Found")
else:
    print("Error")
