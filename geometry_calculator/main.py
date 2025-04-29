# Gabriel Croizer - Geometry Calculator

from shapes import Circle, Rectangle, Square, Triangle  # Uncomment if you have these classes defined in shapes.py
from InquirerPy import inquirer

def main():
    circle = None
    rectangle = None
    square = None
    triangle = None
    print("\033cWelcome to my Geometry Calculator!")

    while True:
        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                "Create a Shape",
                "Compare Shapes",
                "Exit Program"
            ]
        ).execute()

        if action == "Create a Shape":
            shape_type = inquirer.select(
                message="Which shape would you like to create?",
                choices=[
                    "Circle",
                    "Rectangle",
                    "Square",
                    "Triangle"
                ]
            ).execute()

            if shape_type == "Circle":
                radius = inquirer.number(message="Enter the radius of the circle:", float_allowed=True, replace_mode=True).execute()
                circle = Circle(float(radius))
                print(f"\033cCircle created with radius {circle.radius}. Area: {circle.area()}, Perimeter: {circle.perimeter()}")
            elif shape_type == "Rectangle":
                length = inquirer.number(message="Enter the length of the rectangle:", float_allowed=True, replace_mode=True).execute()
                width = inquirer.number(message="Enter the width of the rectangle:", float_allowed=True, replace_mode=True).execute()
                rectangle = Rectangle(float(length), float(width))
                print(f"\033cRectangle created with length {rectangle.length} and width {rectangle.width}. Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
            elif shape_type == "Square":
                side_length = inquirer.number(message="Enter the side length of the square:", float_allowed=True).execute()
                square = Square(float(side_length))
                print(f"\033cSquare created with side length {square.length}. Area: {square.area()}, Perimeter: {square.perimeter()}")
            elif shape_type == "Triangle":
                while True:
                    side_a = inquirer.number(message="Enter side A of the triangle:", float_allowed=True, replace_mode=True).execute()
                    side_b = inquirer.number(message="Enter side B of the triangle:", float_allowed=True, replace_mode=True).execute()
                    side_c = inquirer.number(message="Enter side C of the triangle:", float_allowed=True, replace_mode=True).execute()

                    # Check if the sides form a valid triangle using the triangle inequality theorem
                    if (float(side_a) + float(side_b) > float(side_c) and
                        float(side_a) + float(side_c) > float(side_b) and
                        float(side_b) + float(side_c) > float(side_a)):
                        triangle = Triangle(float(side_a), float(side_b), float(side_c))
                        print(f"\033cTriangle created with sides {triangle.side_a}, {triangle.side_b}, {triangle.side_c}. Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")
                        break
                    else:
                        print("\033cThe two shortest sides summed up must be greater than the longest side to form a triangle. Please try again.")
                print(f"\033cTriangle created with base, sides {triangle.side_a}, {triangle.side_b}, {triangle.side_c}. Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")
        elif action == "Compare Shapes":
            if any([circle, rectangle, square, triangle]):
                print("\033cShape Comparison Chart:")
                print(f"{'Shape':<40}{'Area':<15}{'Perimeter':<15}")
                print("-" * 80)
                if circle:
                    print(f"Circle (radius {circle.radius}):".ljust(40) + f"{circle.area():<15.2f}{circle.perimeter():<15.2f}")
                if rectangle:
                    print(f"Rectangle (length {rectangle.length}, width {rectangle.width}):".ljust(40) + f"{rectangle.area():<15.2f}{rectangle.perimeter():<15.2f}")
                if square:
                    print(f"Square (side {square.length}):".ljust(40) + f"{square.area():<15.2f}{square.perimeter():<15.2f}")
                if triangle:
                    print(f"Triangle (sides: {triangle.side_a}, {triangle.side_b}, {triangle.side_c}):".ljust(40) + f"{triangle.area():<15.2f}{triangle.perimeter():<15.2f}")
                print('\n')
            else:
                print("\033cNo shapes have been created yet to compare.")
        elif action == "Exit Program":
            print("\033cThank you for using my program!")
            return
main()