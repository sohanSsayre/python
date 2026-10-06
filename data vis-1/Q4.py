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

# create fig with 1 row and 2 columns
plt.figure(figsize=(12,5))

# first subplot -bar chart

plt.subplot(1,2,1)
plt.bar(
    df['category'],
    df['Qty Ordered'],
    color='skyblue',
    edgecolor='black'
)

plt.xlabel('product category')
plt.ylabel('unit ordered')
plt.title('product category VS. unit ordered')
plt.xticks(rotation=45)

# second subplot- scatter plot
plt.subplot(1,2,2)

plt.scatter(
    df['unit price'],
    df['Qty Ordered'],
    marker='o',
    s=100,
    alpha=0.6,
    color='skyblue',
    edgecolors='black'   
)

plt.xlabel('unit price')
plt.ylabel('qty ordered')
plt.title('unit price VS. qty ordered')

# adjust spacing
plt.tight_layout()

# display fig

plt.show()