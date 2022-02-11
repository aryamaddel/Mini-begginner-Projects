def identify(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


for i in range(3000):
    if identify(i) == True:
        print(i)
    else:
        continue
