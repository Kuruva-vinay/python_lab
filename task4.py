# Accept lengths of three sides of a triangle as input
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Determine if the triangle is right-angled using the Pythagorean theorem
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
