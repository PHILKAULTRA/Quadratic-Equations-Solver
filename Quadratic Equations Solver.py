import cmath

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Calculate the discriminant
discriminant = (b**2) - (4*a*c)

# Find the roots
root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

# Print the roots
print("The roots of the quadratic equation are:")
print("Root 1: ", root1)
print("Root 2: ", root2)
