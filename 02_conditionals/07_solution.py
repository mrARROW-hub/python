order_size = str(input("Medium\n Small\n Large\n tell us any one :)"));

extra_shot = str(input("Do you want the extra shot?\n True or False: "));

if extra_shot == "True":
    print(order_size +"coffee with an extra shot Ready!");
elif extra_shot == "False":
    print(order_size +"coffee Ready!");
else:
    print(order_size +"coffee Ready!");