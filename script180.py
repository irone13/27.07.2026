import random
random.seed(1)
best_score = None

while True:
    print("I picked a nummber between 1 and 100")
    guesses = 0
    right_num = random.randint(1,100)
    num = int(input("Guess ? "))
    while True :
        if num > right_num:
           print("too high")
        elif num == right_num :
            print (f"Correct ! it took you {guesses +1} guesses")
            break

        else :
          print ("too low")
        guesses +=1
        num = int(input("Guess ? "))

    if best_score is None or best_score > guesses:
        best_score = guesses

    print(f"Your best score is {best_score +1}")
    a = input("Try again ?")
    if a == ('yes'):
        continue
    else:
        break





