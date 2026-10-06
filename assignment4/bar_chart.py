import matplotlib.pyplot as plt

students=["A","B","C","D"]

marks=[85,90,40,22]

plt.bar(students,marks,color="yellow")

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

