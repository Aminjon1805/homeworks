from main import Circle, Rectangle, Square

print("###################################")
print("# S H A P E   C A L C U L A T O R #")
print("###################################\n")

print("Menu:\n| Rectangle | Circle | Square |\n")
while True:

    shape = input("Which shape you wanna choose (type Exit to exit): ")
    print("\n")

    if shape.lower() == "circle":

        radius = float(input("Magnitude of the radius: "))
        area = Circle(radius).area()
        perimetr = Circle(radius).perimetr()

        print(f"{area}\n{perimetr}\n")

    elif shape.lower() == "rectangle":

        length = float(input("Magnitude of length: "))
        width = float(input("Magnitude of width: "))

        area = Rectangle(length, width).area()
        perimetr = Rectangle(length, width).perimetr()

        print(f"{area}\n{perimetr}\n")

    elif shape.lower() == "square":

        side = float(input("Magnitude of side: "))

        area = Square(side).area()
        perimetr = Square(side).perimetr()

        print(f"{area}\n{perimetr}\n")



    elif shape.lower() == "exit":

        print("Thanks for using 😁, you are the best \n (☞ﾟヮﾟ)☞   (⌐■_■)   ☜(ﾟヮﾟ☜)")
        break

    else:
        print("Invalid shape!!!")


