import random
pc = 0
user  = 0
while pc or user <= 5  :
    if user >= 5 :
        print("the winner is the User ")
    if pc >= 5 :
        print("the winner is the PC")
    else :
        random_number = random.randint(1, 100)
        print("to show rules enter rules \nthis is a battle with the PC and the human kind ")
        for attempt in range(3):
            num1 = input("Please enter your desired number : ")
            while num1 == "rules" :
                print("""the rules \n1.if you guess the correct number you get 2 point \n2.if you guess the number with in 5 attempts you get on point """
                      "\n3.if you dont guess the number with in 5 attempts the PC gats 1 point \n4.whose reach 5 point firsts win the game ")
                num1 = (input("Please enter your desired number : "))
            if num1.isdigit() :
                num1 = int(num1)

            if num1 == random_number:
                print("Congratulations! You guessed the correct number.")
                user += 2
                break
            elif abs(num1 - random_number) <= 10:
                print("Good guess! Your number was close to the real number.")
                user += 1
                break
            else:
                print("Your guess was not close. Try again.")
            attempt -= 3

        else:
            print(f"Sorry, you've used all your attempts. The correct number was {random_number}.")
            pc += 1


    print(f"PC :{pc}\nUser : {user}")
