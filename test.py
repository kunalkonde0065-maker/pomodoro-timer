#Typing the number

num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))

#printing the operation

print("=====Select The Operation=====")
print("1) Addition (+)")
print("2) Subtraction (-)")
print("3) Multiplication (*)")
print("4) Division (/)")

# chosing the operation

choice = input("Enter your option (1/2/3/4): ")

#calculations

if choice == "1":
    result = num1 + num2
    print("The result is: ",result)
elif choice == "2":
    result = num1 - num2
    print("The result is: ",result)
elif choice == "3":
    result = num1 * num2
    print("The result is: ",result)
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("The result is: ",result)
    else:
        print("error,Division by zero not possible")
else:
    print("Invalid option,choose correct option")
