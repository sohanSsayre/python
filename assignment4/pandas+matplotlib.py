import pandas as pd
import matplotlib.pyplot as plt

data={
    'month':['jan','feb','mar','apr'],
    'sales':[200,250,300,280]
}

df=pd.DataFrame(data)

plt.plot(df['month'],df['sales'],marker='o')
plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid(True)
plt.show()