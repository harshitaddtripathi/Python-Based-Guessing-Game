import random
random_num = random.randint(1,10)
user = None
gusses=0
while(user != random_num):
    user = int(input("Enter the number : "))
    if user == random:
        print("You have Entered the correct number : ", user)
    else:
        if user>random_num:
            print("You have entered greater number")
        else:
            print("You have entered Smaller number")
    gusses+=1
print(f"You have gussesed in {gusses} gusses.")
