import time
print("Hi There, My name is Calc and I do multiplication for you!")

def calculator():
    x=input("Enter First Value")
    y=input("Enter Second Value")
    z=int(x)*int(y)
    time.sleep(2)
    print(f"your Answer is {z}")


calculator()