number_of_characters = int(input("How many characters are there in your Password? 🤔"));

if number_of_characters <= 6:
    print("Your password is Weak");
elif number_of_characters <= 10:
    print("Your password is Fine :)");
else:
    print("Your password is preety Strong!!");