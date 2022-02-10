list = [12, 45, 67, 89, 99, 100]  # sorted list

# numbner to search
number = 100


def search(list, n):
    low = 0
    high = len(list)-1
    mid = 0

    while low <= high:
        mid = (low+high)//2
        if list[mid] == n:
            return mid
        elif list[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1


search_result = search(list, number)
if search_result != -1:
    print('Element found at : ', search_result)
elif search_result == -1:
    print("Element NOT Found")
else:
    print("Error")
