#Starting Intro.
while True:
    print("Welcome To General Question Asking Software.")

    #User input of information abou him/her.
    X= input("Enter Your Name :") 
    print("Welcome", X)  
    Y= int(input("Enter Your Age :"))  
    Z= input("Are You A 'Boy' Or 'Girl' ?")
    W= int(input("Enter Your Weight in Kg:"))

    #Information For Functioning.
    print("Ask one of the given questions :-")
    print("Format : Question - Input")
    print("Am I eligible to vote? - A")
    print("Am I eligible to marry? - B")
    print("Am I eligible to work to earn? - C")
    print("Am I eligible to apply for Passport? - D")
    print("Am I eligible to Donate Blood? - E")

    #User Input Command.
    Q = input("What do you want to ask?")

    #Processing Part 1
    if Q=="A":
        if Y >= 18 :
            print("Yes , Of Course !!")
        else :
            print("No. You need to wait for",(18 - Y),"years more.")

    #Processing Part 2
    if Q=="B" and Z=="Boy" :
         if Y >= 18 :
            print("Yes , Of Course !!")
         else :
            print("No. You need to wait for",(21 - Y),"years more.")
    if Q=="B" and Z=="Girl" :
         if Y >= 18 :
            print("Yes , Of Course !!")
         else :
            print("No. You need to wait for",(18 - Y),"years more.")

    #Processing Part 3
    if Q=="C":
        if Y>= 18 :
            print("Yes , Of Course !!")
        if Y>= 14 and Y<18:
            print("You can do non-hazardous work only for",(18 - Y),"years.")
        else :
            print("No, otherwise the work owner will go to jail.")

    #Processing Part 4
    if Q=="D":
        if Y>= 18 :
            print("Yes , Of Course !!")
        else :
            print("Yes, but only under parental consent.")

    #Processing Part 5
    if  Q=="E":
        if Y>=18 and W>=50:
             print("Yes , Of Course !!")
        if Y>=18 and W<50:
            print("No, Weight must be more than 50kg.")
        else:
            print("Age must be more than 18years.")

 # Ask user if they want to continue or exit
    cont = input("Do you want to Restart? (Yes/No): ")
    if cont != "Yes":
        print("Thank you for using the software. Goodbye!")
        break  # Exit the loop
    
#Made by Aditya Ranjan , 9th A.

 








