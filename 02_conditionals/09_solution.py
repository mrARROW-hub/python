year = int(input("Which year do you want to check? 😁 :"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("That's a leap year :)");
else:
    print("No, its not a leap year :/");
