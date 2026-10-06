import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'Category': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard'],
    'Qty Ordered': [30, 60, 35, 50, 25],
    'Unit Price': [55000, 20000, 30000, 2500, 1500]
}

df = pd.DataFrame(data)

# Create figure with 1 row and 2 columns
plt.figure(figsize=(12, 5))

# First subplot - Bar chart
plt.subplot(1, 2, 1)

plt.bar(
    df['Category'],
    df['Qty Ordered'],
    color='skyblue',
    edgecolor='black'
)

plt.xlabel('Product Category')
plt.ylabel('Units Ordered')
plt.title('Product Category vs. Units Ordered')
plt.xticks(rotation=45)

# Second subplot - Scatter plot
plt.subplot(1, 2, 2)

plt.scatter(
    df['Unit Price'],
    df['Qty Ordered'],
    marker='o',
    s=100,
    alpha=0.6,
    color='green',
    edgecolor='black'
)

plt.xlabel('Unit Price')
plt.ylabel('Units Ordered')
plt.title('Unit Price vs. Units Ordered')

# Adjust spacing
plt.tight_layout()

# Display figure
plt.show()