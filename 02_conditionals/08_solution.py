password = input("pls enter your password :");

if len(password) < 6:
    print("Your password is too weak! :/\n learn now to make a strong password by our website :)");
elif len(password) < 10:
    print("Your password is completely fine :)");
else:
    print("Your password is preety strong, Well Done!\n you realy look out for safety. :)");