# Accept a number from 1-7 and give the subsequent day of the week where 1 = Sunday and 7 = Saturday

number = int(input("Enter an integer from 1 to 7: "))

weekdays = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday",
}

if number >= 1 and number <= 7:
    print (weekdays[number])
elif number < 1 or number > 7:
    statement = "There is no \"{}\" day in the week"
    print (statement.format(number))
else:
    print ("Unknown error")