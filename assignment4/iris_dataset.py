import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\sohan\Desktop\python\collage assiment\assignment4\Iris.csv")
print("First 5 records :")
print(df.head())
# display dataset records
print("\nDataset Information :")
print(df.info())
# display statistical summary
print("\nStatistical Summary :")
print(df.describe())
#check missing values
print("\nMissing Values :")
print(df["Species"].value_counts())
# ------------Matplotlib Operations --------------------
# line plot
plt.figure(figsize=(6,4))
plt.plot(df["SepalLengthCm"])
plt.title("Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
# bar chart
species=df["Species"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(species.index, species.values)
plt.title("Species Count ")
plt.xlabel("Species")
plt.ylabel("Count")
#Histogram
plt.figure(figsize=(6,4))
plt.hist(df["PetalLengthCm"],bins=10)
plt.title("Petal Length Histogram")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()
#Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["SepalLengthCm"],df["PetalLengthCm"])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()