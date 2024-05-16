import time
name=input("Hello there, What is your name?")
print(f"Hey {name}, nice to meet you!, let's play the Riddle Game")
print()
ans= input("Are you ready? Press Y or N")

if ans.upper()=='Y':
    print("Awesome, lets start!")
else:
    print("Get ready boyo!")

ans1=input("What do you call a bear with no teeth?")
if ans1=='gummy bear':
    print("Awesome!")
else:
    print(f"{ans1} is incorrect, the right answer is A gummy bear!")

time.sleep(2)
print("Ok, one more for you!")
ans2=input("What question can you never answer yes to?")
if ans =="are you asleep yet?":
    print("Awesome!")
else:
    print(f"{ans2} is not right, the right answer is: Are you Asleep yet? ")

time.sleep(2)
print("Ok, one more for you!")
ans2=input(" What kind of lion never roars?")
if ans =="dandelion":
    print("Awesome!")
else:
    print(f"{ans2} is not right, the right answer is: dandelion ")

v1=input("Want one more?")
if v1.upper()=='Y':
    print("Alright, here you go!")
else:
    exit()

time.sleep(2)
print("Ok, here you go!")
ans2=input("It belongs to you, but your friends use it more. What is it?")
if ans =="name":
    print("Awesome!")
else:
    print(f"{ans2} is not right, the right answer is: Your Name! ")

time.sleep(3)
print("Hope you Enjoyed this! bye bye")
k=input("Press any key to close!")