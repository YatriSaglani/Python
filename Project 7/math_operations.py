import math


def Math_Operations_Task():

    while True:
        print("\n1.Calculate factorial of a number")
        print("2.Solve compound interest")
        print("3.Trigonometric operations")
        print("4.Area of geometric shapes")
        print("5.Back to main menu\n")

        choice = int(input("Choose an option : "))

        match choice:

            case 1:
                num = int(input("Enter a number: "))

                factorial = 1

                for i in range(1, num + 1):
                    factorial = factorial * i

                print("Factorial =", factorial)

            case 2:
                principal = float(input("Enter the principal amount: "))
                rate = float(input("Enter the annual interest rate (in %): "))
                time = float(input("Enter the time (in years): "))

                compound_interest = principal * (1 + rate / 100) ** time

                print("Compound Interest =", compound_interest)

            case 3:
                angle = float(input("Enter an angle in degrees: "))

                radians = math.radians(angle)

                print("Sine:", math.sin(radians))
                print("Cosine:", math.cos(radians))
                print("Tangent:", math.tan(radians))

            case 4:
                print("1.Area of Circle")
                print("2.Area of Rectangle")
                print("3.Area of Triangle")

                shape_choice = int(input("Choose a shape: "))

                match shape_choice:

                    case 1:
                        radius = float(input("Enter the radius of the circle: "))
                        area_circle = math.pi * radius ** 2
                        print("Area of Circle =", area_circle)

                    case 2:
                        length = float(input("Enter the length of the rectangle: "))
                        width = float(input("Enter the width of the rectangle: "))
                        area_rectangle = length * width
                        print("Area of Rectangle =", area_rectangle)

                    case 3:
                        base = float(input("Enter the base of the triangle: "))
                        height = float(input("Enter the height of the triangle: "))

                        area_triangle = 0.5 * base * height

                        print("Area of Triangle =", area_triangle)

            case 5:
                print("Returning to main menu...")
                break


if __name__ == "__main__":
    Math_Operations_Task()