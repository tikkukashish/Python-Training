# calculate area,param,circumference of rectangle,square,circle,trapezium,parallelogram,rhombus

#menu based program 

def AreaRectangle():
    rectangle_length=int(input("Enter the length of rectangle: "))
    rectangle_width=int(input("Enter the width of rectangle: "))
    rectangle_area=rectangle_length*rectangle_width
    print(f"Area of rectangle: {rectangle_area}")
    print(f"Perimeter of rectangle: {2*(rectangle_length+rectangle_width)}")

def AreaCircle():
    circle_radius=int(input("Enter the radius of circle: "))
    circle_area=3.14*circle_radius**2
    circle_circumference=2*3.14*circle_radius
    print(f"Area of circle: {circle_area}")
    print(f"Circumference of circle: {circle_circumference}")

def AreaSquare():
    square_side=int(input("Enter the side of square: "))
    square_area=square_side**2
    square_perimeter=4*square_side
    print(f"Area of square: {square_area}")
    print(f"Perimeter of square: {square_perimeter}")

def AreaTrapezium():
    trapezium_base1=int(input("Enter the base1 of trapezium: "))
    trapezium_base2=int(input("Enter the base2 of trapezium: "))
    trapezium_height=int(input("Enter the height of trapezium: "))
    trapezium_area=0.5*(trapezium_base1+trapezium_base2)*trapezium_height
    print(f"Area of trapezium: {trapezium_area}")
    print(f"Perimeter of trapezium: {trapezium_base1 + trapezium_base2 + 2 * ((trapezium_height ** 2) + ((trapezium_base2 - trapezium_base1) / 2) ** 2) ** 0.5}")

def AreaParallelogram():
    parallelogram_base=int(input("Enter the base of parallelogram: "))
    parallelogram_height=int(input("Enter the height of parallelogram: "))
    parallelogram_side=int(input("Enter the side of parallelogram: "))
    parallelogram_area=parallelogram_base*parallelogram_height
    print(f"Area of parallelogram: {parallelogram_area}")
    print(f"Perimeter of parallelogram: {2*(parallelogram_base+parallelogram_side)}")

def AreaHexagon():
    hexagon_side=int(input("Enter the side of hexagon: "))
    hexagon_area=(3*(3**0.5)*hexagon_side**2)/2
    hexagon_perimeter=6*hexagon_side
    print(f"Area of hexagon: {hexagon_area}")
    print(f"Perimeter of hexagon: {hexagon_perimeter}")

def AreaRhombus():
    rhombus_diagonal1=int(input("Enter the first diagonal of rhombus: "))
    rhombus_diagonal2=int(input("Enter the second diagonal of rhombus: "))
    rhombus_area=0.5*rhombus_diagonal1*rhombus_diagonal2
    print(f"Area of rhombus: {rhombus_area}")
    print(f"Perimeter of rhombus: {4 * ((rhombus_diagonal1 ** 2 + rhombus_diagonal2 ** 2) ** 0.5)}")


print("1. Rectangle")
print("2. Circle")
print("3. Square")
print("4. Trapezium")
print("5. Parallelogram")
print("6. Rhombus")
print("7. Hexagon")
print("8. Exit")

while(True):
    choice=int(input("Enter your choice: "))

    if choice==1:
        AreaRectangle()

    elif choice==2:
        AreaCircle()

    elif choice==3:
        AreaSquare()

    elif choice==4:
        AreaTrapezium()

    elif choice==5:
        AreaParallelogram()

    elif choice==6:
        AreaRhombus()

    elif choice==7:
        AreaHexagon()

    elif choice==8:
        print("Exiting the program.")
        break
