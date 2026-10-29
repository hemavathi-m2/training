import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# File paths
base_path = Path(__file__).parent
graph_path = base_path / "graphs"
graph_path.mkdir(parents=True, exist_ok=True)

# 1. NumPy
marks = np.array([[80, 75, 90], [65, 85, 70], [90, 95, 85], [70, 60, 80]])

print("Shape:", marks.shape)

student_avg = np.mean(marks, axis=1)
print("Student averages:", np.round(student_avg, 2))

subject_avg = np.mean(marks, axis=0)

grace_marks = marks + 5

weights = np.array([0.5, 0.3, 0.2])
weighted_scores = np.dot(marks, weights)

# 2. Load CSV files

df = pd.read_csv(base_path / "employees.csv")
departments = pd.read_csv(base_path / "departments.csv")

print("\nDataFrame Info:")
df.info()

loc=df.loc[0:2, ["name", "salary"]]

iloc=df.iloc[0:3, 0:3]

# 3. Data Cleaning

median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

df = df.drop_duplicates().copy()

# Correct data types
df["id"] = df["id"].astype("int64")
df["salary"] = df["salary"].astype("float64")

for column in ["name", "department", "city"]:
    df[column] = df[column].astype("string").str.strip()

departments["department"] = departments["department"].astype("string").str.strip()
departments["head"] = departments["head"].astype("string").str.strip()
departments["budget"] = departments["budget"].astype("int64")

# 4. Groupby and Aggregation

summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"),
)

headcount = summary["headcount"]
print(
    "\nHeadcount:",
    " | ".join(f"{dept} {int(count)}" for dept, count in headcount.items()),
)


# 5. Inner, Left and Outer Joins

inner_join = pd.merge(df, departments, on="department", how="inner")

left_join = pd.merge(df, departments, on="department", how="left")

outer_join = pd.merge(df, departments, on="department", how="outer", indicator=True)


dept_without_employees = departments.loc[
    ~departments["department"].isin(df["department"]), "department"
].tolist()

print("\nOuter join: department with no employees listed:", dept_without_employees)


# 6. Bar Chart

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar", label="Average Salary")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig(graph_path / "bar_chart.png")
plt.close()

# 7. Histogram
plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, edgecolor="black", label="Employees")

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig(graph_path / "histogram.png")
plt.close()

# 8. Scatter Plot
plt.figure(figsize=(8, 5))

for department in df["department"].unique():
    group = df[df["department"] == department]
    plt.scatter(group["id"], group["salary"], label=department)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.tight_layout()
plt.savefig(graph_path / "scatter_plot.png")
plt.close()

# 9. Line Chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))
plt.plot(months, monthly_sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig(graph_path / "line_chart.png")
plt.close()
