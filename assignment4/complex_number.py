import numpy as np
arr=np.array([2+3j,4+5j,6+2j,1+4j])

print("array of complex numbers:")
print(arr)

total=np.sum(arr)

total_sub = np.subtract.reduce(arr)

total_prod = np.prod(arr)

total_div = np.divide.reduce(arr)

print("sum of all complex numbers:",total)
print("sub of all complex numbers:",total_sub)
print("multiplication of all complex numbers:",total_prod)
print("division of all complex numbers:",total_div)
# print(total)