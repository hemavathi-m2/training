import pandas as pd

df=pd.read_csv("employees.csv")
print("employee_details:\n",df)
print("head:\n",df.head())
print("info:\n",df.info())
print("describe:\n",df.describe())

print("name:\n",df["name"].to_string(index=False))
print("name and salary:\n",df[["name","salary"]].to_string(index=False))

city=(df.loc[df["city"]=="Chennai","name"])
print("Chennai :",",".join(city))

print("slice:\n",df.iloc[0:3 , 1:3].to_string(index=False))

high_salary=df[df["salary"]>50000]
print("Salary above 50000:",len(high_salary),"employees")

it_employees=df[df["department"]=="IT"]

print("IT department:",",".join(it_employees["name"]))


