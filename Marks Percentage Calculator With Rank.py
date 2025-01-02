#Marks Percentage Calculator With Rank

while True:
    def percy(a, b):
        return ((a+b)/240)*100

#Detailing First User 
    
    S1 = input("Enter The Name Of First Student:")
    M1 = int(input("Enter Your English's Marks:"))
    M2 = int(input("Enter Your Hindi's Marks:"))
    M3 = int(input("Enter Your Math's Marks:"))
    M4 = int(input("Enter Your Science's Marks:"))
    M5 = int(input("Enter Your Social Scienece's Marks:"))
    M6 = int(input("Enter Your Computer's Marks:"))

    X1 = (M1 + M2 + M3)
    Y1 = (M4 + M5 + M6)
    Z1 = percy(X1, Y1)

#Detailing Second User

    S2 = input("Enter The Name Of Second Student:")
    M7 = int(input("Enter Your English's Marks:"))
    M8 = int(input("Enter Your Hindi's Marks:"))
    M9 = int(input("Enter Your Math's Marks:"))
    M10 = int(input("Enter Your Science's Marks:"))
    M11 = int(input("Enter Your Social Scienece's Marks:"))
    M12 = int(input("Enter Your Computer's Marks:"))

    X2 = (M7 + M8 + M9)
    Y2 = (M10 + M11 + M12)
    Z2 = percy(X2, Y2)

#Detailing Third User

    S3 = input("Enter The Name Of Third Student:")
    M13 = int(input("Enter Your English's Marks:"))
    M14 = int(input("Enter Your Hindi's Marks:"))
    M15 = int(input("Enter Your Math's Marks:"))
    M16 = int(input("Enter Your Science's Marks:"))
    M17 = int(input("Enter Your Social Scienece's Marks:"))
    M18 = int(input("Enter Your Computer's Marks:"))

    X3 = (M13 + M14 + M15)
    Y3 = (M16 + M17 + M18)
    Z3 = percy(X3, Y3)

#Calculation Of Rank And Print Percentage

    if Z1==Z2 and Z2==Z3:
        print("All Got Same!!")

    elif Z1==Z2>Z3:
        print(S1,"and",S2,"got same marks and",S3,"is third.")

    elif Z1==Z2<Z3:
        print(S1,"and",S2,"got same marks and",S3,"is first.")

    elif Z2==Z3>Z1:
        print(S2,"and",S3,"got same marks and",S1,"is third.")

    elif Z2==Z3<Z1:
        print(S2,"and",S3,"got same marks and",S1,"is first.")

    elif Z1==Z3>Z2:
        print(S1,"and",S3,"got same marks and",S2,"is third.")

    elif Z1==Z3<Z2:
        print(S1,"and",S3,"got same marks and",S2,"is first.")        

    elif Z1>Z2 and Z2>Z3:
        print(S1,"is first with",Z1,"percentage.")
        print(S2,"is second with",Z2,"percentage.")
        print(S3,"is third with",Z3,"percentage.")

    elif Z1>Z3 and Z3>Z2:
        print(S1,"is first with",Z1,"percentage.")
        print(S2,"is second with",Z3,"percentage.")
        print(S3,"is third with",Z2,"percentage.")

    elif Z2>Z1 and Z1>Z3:
        print(S1,"is first with",Z2,"percentage.")
        print(S2,"is second with",Z1,"percentage.")
        print(S3,"is third with",Z3,"percentage.")

    elif Z2>Z3 and Z3>Z1:
        print(S1,"is first with",Z2,"percentage.")
        print(S2,"is second with",Z3,"percentage.")
        print(S3,"is third with",Z1,"percentage.")

    elif Z3>Z2 and Z2>Z1:
         print(S1,"is first with",Z3,"percentage.")
         print(S2,"is second with",Z2,"percentage.")
         print(S3,"is third with",Z1,"percentage.")

    elif Z3>Z1 and Z1>Z2:
        print(S1,"is first with",Z3,"percentage.")
        print(S2,"is second with",Z1,"percentage.")
        print(S3,"is third with",Z2,"percentage.")

    else :
        print("Something Is Wrong , Error707 !!!")

#Loop Optional Choosing !!!   

    A= input("Would you like to use it again?[Y/N]:")
    if A == 'N':
        print("Thank You!!!")
        break
    elif A == "Y":
        continue
    else:
        print("Invalid Choice. Thank You!!")
        break

#Made By Aditya Ranjan
