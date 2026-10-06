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
print("local tech stor data:")
print(df)

# bar chartg
plt.bar(
    df['category'],
    df['Unit sold'],
    color='skyblue',
    edgecolor='black'
)

# chart details
plt.xlabel('category')
plt.ylabel('Ubnit sold')
plt.title('Unit sold across categories')

# display chart
plt.show()