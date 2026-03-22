fruit = str(input("what fruit do you want to check to check :"));

fruit_color = str(input("tell me the color of your fuit :"));

if fruit == "banana":
    if fruit_color == "yellow":
        print("ripe!");
    elif fruit_color == "green":
        print("underripe");
    elif fruit_color == "brown":
        print("overripe");
else:
    print("i don't know that!!!  :/");