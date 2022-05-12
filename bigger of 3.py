# Display the biggest of 3 numbers

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print (num1)
elif num2 > num1 and num2 > num3:
    print (num2)
elif num3 > num1 and num3 > num2:
    print (num3)
else:
    print ("2 or more numbers are equal")