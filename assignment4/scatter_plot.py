import matplotlib.pyplot as plt

hours_studied=[1,2,3,4,5,6]

marks=[35,40,50,55,65,75]

plt.scatter(hours_studied,marks,color="red")

plt.title("Study Hours VS Marks")
plt.xlabel("Hours studied")
plt.ylabel("marks")
plt.show()