# Accept 2 numbers and output the bigger number
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

if num1 > num2:
    print (num1)
elif num2 > num1:
    print (num2)
else:
    print ("They are the same number?")