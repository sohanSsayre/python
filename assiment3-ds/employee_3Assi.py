import pandas as pd
# read and display csv file
df=pd.read_csv(r"C:\Users\sohan\Desktop\python\collage assiment\assiment3-ds\employee.csv")

print("original data:")
print(df)

# disply mising values

print("\nrecords with mising values:")
print(df[df.isnull().any(axis=1)])

# add new row
new_employee={
    "eid":107,
    "ename":"rohan",
    "edesig":"engineer",
    "esal":50000,
    "ddept":"production"
}

df.loc[len(df)]=new_employee
print("\nData after adding new row:")
print(df)

# find avg salary
avrage_salary=df["esal"].mean()

print("\naverage salary:",avrage_salary)

# replace mising salary with mean

# df["esal"].fillna(avrage_salary,inplace=True)

df["esal"] = df["esal"].fillna(avrage_salary)

print("\ndata after replacing mising values:")

print(df)

# display ename,esal,edept
print("\nemployee name,salary,depertement:")
print(df[["ename","esal","ddept"]])

# drop row with missing values
clean_df=df.dropna()
print("\ndata after droping mising values:")
print(clean_df)

# remove a specific row
df=df[df["eid"]!=104]

print("\ndata after removing eid=104:")
print(df)
