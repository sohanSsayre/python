import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])


addition = A + B
subtraction = A - B
Multiplication = A * B
Product = A / B  

print("Addition:\n", addition)
print("\nSubtraction:\n", subtraction)
print("\nMultiplication:\n", Multiplication)
print("\nProduct (Matrix Multiplication):\n", Product)