import pandas as pd
# print(pd.__version__)

# series 

# data = [1,2,3,4,5]
# print(pd.Series(data))  

employees = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Naveen", "Priya", "Rahul", "Suresh", "Anitha", "Karthik", "Divya"],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Sales", "Finance"],
    "Salary": [55000, 48000, 72000, 61000, 45000, 53000, 69000],
    "Experience": [3, 5, 8, 4, 2, 6, 7],
    "City": ["Chennai", "Bangalore", "Hyderabad", "Chennai", "Coimbatore", "Delhi", "Mumbai"]
}
df = pd.DataFrame(employees)

# print(df.head(3))  

# print(df.tail(2))

# print(df.columns)

# print(type(df))

# print(df["Name"].iloc[df['Salary'].idxmax()])

# print(df["Salary"].mean())

# print(df[df["Department"]=="IT"]) 

# sal = df[df["Salary"]>60000]
# print(sal)

df["Bonus"] = df["Salary"] * 0.1

df["Annual Salary"] = df["Salary"]*12

sortedsal = df.sort_values(by="Salary", ascending=False)

# print(df.groupby("Department").count()["Emp_ID"])

# m_exp = df["Name"].iloc[df['Experience'].idxmax()]
# print(m_exp)

# print(df[["Name", "Salary"]])

sortedsal.to_csv("pandas/sorted_salary.csv", index=False)