import pandas as pd
import numpy as np

data1 = {
    'Emp_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['IT', 'HR', 'IT', np.nan, 'HR', 'Sales'],
    'Salary': [70000, 50000, np.nan, 60000, 52000, 45000],
    'Experience_Years': [5, 3, 4, np.nan, 2, 1]
}

df1 = pd.DataFrame(data1)
print("--- Initial DataFrame ---")
print(df1)


print("\n--- Numerical Summary ---")
print(df1.describe())

print("\n--- Concise Info (Data types & non-null counts) ---")
df1.info()

# generly use of group
avg_salary_by_dept = df1.groupby('Department')['Salary'].mean()

print("--- Average Salary by Department ---")
print(avg_salary_by_dept)

# using agg
dept_summary = df1.groupby('Department').agg(
    Employee_Count=('Emp_ID', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Total_Experience=('Experience_Years', 'sum')
)

print("\n--- Department Summary ---")
print(dept_summary)


data2 = {
    'Emp_ID': [107, 108],
    'Name': ['Grace', 'Hank'],
    'Department': ['Sales', 'IT'],
    'Salary': [48000, np.nan],  
    'Experience_Years': [2, 6]
}

df2 = pd.DataFrame(data2)

combined_df = pd.concat([df1, df2], ignore_index=True)

print("--- Combined DataFrame (after Concatenation) ---")
print(combined_df)

# # 1. Check for NaNs across the whole DataFrame (returns True/False grid)
print("--- Is NaN Grid ---")
print(combined_df.isna())

# # 2. Count missing values column-wise (most practical method)
print("\n--- Missing Value Count per Column ---")
print(combined_df.isna().sum())

# # # 3. Filter and view only the rows with missing values
missing_rows = combined_df[combined_df.isna().any(axis=1)]
print("\n--- Rows containing at least one NaN ---")
print(missing_rows)



# Create a copy so we don't overwrite the original
df_filled = combined_df.copy()

# 1. Fill missing Department with 'Unknown'
df_filled['Department'] = df_filled['Department'].fillna('Unknown')

# 2. Fill missing Salary with the mean salary
mean_salary = df_filled['Salary'].mean()
df_filled['Salary'] = df_filled['Salary'].fillna(mean_salary)

# 3. Fill missing Experience_Years with the median experience
median_exp = df_filled['Experience_Years'].median()
df_filled['Experience_Years'] = df_filled['Experience_Years'].fillna(median_exp)

print("--- DataFrame after Filling NaNs ---")
print(df_filled)
