from random import randint

upper = 20
lower = 1


print("Think of any number between 1 and 20")

while True:
    guess_number = randint(lower, upper)
    feedback = input(f"\nIs the number - {guess_number} Higher(H) or Lower(L) or Correct(C)").lower()

    if feedback == "c":
        print("\nYAY! I won\n")
        exit()
    elif feedback == 'h':
        upper = guess_number-1
        continue
    elif feedback == 'l':
        lower = guess_number+1
        continue