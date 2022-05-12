# Input a year and check if it is a leap year or not

year = int(input("Enter a year: "))

if year % 4 == 0:
    print ("This is a leap year")
else:
    print ("This is a non-leap year")