import pandas as pd
import matplotlib.pyplot as plt

#creat DataFrame
data={
    'category':['laptop','mobile','Tablet','Headphone','keyboard'],
    'Unit sold':[25,50,30,45,20],
    'Qty Ordered':[30,60,35,50,25],
    'unit price':[55000,20000,300000,2500,1500]
}
df=pd.DataFrame(data)

# display dataframe
# print("local tech stor data:")
# print(df)

# set fig size
plt.figure(figsize=(10,5))

# create scatter plot
plt.scatter(
    df['unit price'],
    df['Unit sold'],
    marker='x',
    s=100,
    alpha=0.1,
    color='blue',
    edgecolors='black'
)

# label
plt.xlabel('unit prise')
plt.ylabel('total unit sold')
plt.title('unit price Vs. Total Units Sold')

# add grid
plt.grid(True,alpha=1.0)

# display
plt.show()
