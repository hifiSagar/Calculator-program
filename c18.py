#SIMPLE CALCULATOR

print("simple Calculator")
print("Select One Option")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("0.End the program")

while True:
    operation = int(input("Enter a Choice (1/2/3/4/0)>>  "))
    num1 = int(input("Enter num1>> "))
    num2 = int(input("Enter num2>>  "))
    
    if operation ==1:
        print(num1+num2)
    elif operation ==2:
        print(num1-num2)
    elif operation ==3:
        print(num1/num2)
    elif operation ==4:
        print(num1*num2)
    elif operation == 0:
        print("End the program")
    else:
        print("invalid choice!..Try again!?!..")
            
            