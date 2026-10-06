import numpy as np

arr=np.array([
    [10,20,30],
    [40,np.nan,60],
    [20,40,30]  
])

print("array1:")
print(arr)

arr=np.nan_to_num(arr,nan=0)
print("array after nan_to_num:")
print(arr)


arr2=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("array2:")
print(arr2)
# add
print("addition:")
print(arr+arr2)

# sub
print("sub:")
print(arr-arr2)

# multi
print("multi:")
print(arr*arr2)

# div
print("div:")
print(arr/arr2)

print("\nUnique values:")
print(np.unique(arr))

# index
value=9
index=np.argwhere(arr2==value)
print(f"\n index of value{value}:")
print(index)

# count similar values
values,count=np.unique(arr2,return_counts=True)

print("\n count of similar values:")
for v,c in zip(values,count):
    print(f"{v} occurs {c} times(s)")

