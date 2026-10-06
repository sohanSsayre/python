import pandas as pd



data = {
    "Date": pd.date_range(start="2026-01-01", periods=7, freq="D"),
    "Food_Item": ["Poha", "Avocado toast", "Poha", "Oatmeal Upma", "Dosa", "Smoothie Bowl", "Maggi"],
    "Weekly_Frequency": [4, 2, 4, 3, 2, 5, 1]
}


df = pd.DataFrame(data)
print(df)

print("rows:",df.shape[0])
print("Colums:",df.shape[1])

food_series=df["Food_Item"]
food_dataframe=food_series.to_frame()
print(food_dataframe)


new_rows=pd.DataFrame({
    "Date":["2027-01-01","2027-02-01"],
    "Food_Item":["Sprouts","fruit salad"],
    "Weekly_Frequency":[1,3]
})

new_rows["Date"]=pd.to_datetime(new_rows["Date"])

df=pd.concat([df,new_rows],ignore_index=True)

print(df)

# avg freq
print("average freq:",df["Weekly_Frequency"].mean())

# max freq
print("max freq:",df["Weekly_Frequency"].max())

# min freq
print("min freq:",df["Weekly_Frequency"].min())

# duplicate
duplicates=df[df["Food_Item"].duplicated()]
print(duplicates)

# to replace duplicate food items

replacement={
    "Poha":"Millet Upma"
}
df["Food_Item"]=df["Food_Item"].replace(replacement)

print(df)