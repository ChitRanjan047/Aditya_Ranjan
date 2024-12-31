import math
# Sphere Area And Volume Calculator

print("Welcome To Sphere Area And Volume Calculator.")

while True:
    R = int(input("Enter The Value Of Radius:"))
    X = 4*math.pi*R*R
    Y = (4/3)*math.pi*R*R*R
    print('''Choose An Action :
            1.Surface Area - A
            2.Volume - V ''')
    Action = input("What Do You Want To Do?")
    if Action=='A' :
        print("Answer:", X)
    elif Action=='V' :
        print("Answer:", Y)
    else :
        print("Command Undefined.")

    Z = input("Do you want to calculate again?[Y/N]")

    if Z=='N':
        print("Thank You!!!")
        break
    else:
        continue

