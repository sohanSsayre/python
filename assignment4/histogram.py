import matplotlib.pyplot as plt

ages=[18,19,20,20,21,22,22,23,25,26,24]

plt.hist(ages,bins=5,color="yellow",edgecolor="black")

plt.title("age distribution")
plt.xlabel("Age")
plt.ylabel("frequency")

plt.show()