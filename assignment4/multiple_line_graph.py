import matplotlib.pyplot as plt

months=[1,2,3,4,5]

sales_2024=[100,120,140,160,180]
sales_2025=[110,130,150,170,200]

plt.plot(months,sales_2024,label="2024")
plt.plot(months,sales_2025,label="2025")

plt.title("sales Comparison")
plt.xlabel("month")
plt.ylabel("sales")

plt.legend()

plt.show()