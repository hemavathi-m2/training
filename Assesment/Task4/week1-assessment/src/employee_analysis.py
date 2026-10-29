#!/usr/bin/env python
# coding: utf-8

# 
# # Employee Data Analysis
# 
# This project analyses employee salary data using Python, Pandas, and Matplotlib.
# 
# ## 1. Load Dataset
# 
# ## 2. Explore Employee Data
# 
# ## 3. Salary Analysis
# 
# ## 4. Data Visualization
# 
# ## 5. Key Findings
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/employees.csv")

print(df.head())


# In[2]:


print("Dataset shape:", df.shape)

print("\nColumn details:")
df.info()

print("\nSalary statistics:")
print(df["salary"].describe())


# In[3]:


print("Average salary by department:")

print(df.groupby("department")["salary"].mean())

print("\nHighest salary:")
print(df.loc[df["salary"].idxmax(), ["name", "salary"]])

print("\nLowest salary:")
print(df.loc[df["salary"].idxmin(), ["name", "salary"]])


# In[4]:


avg_salary = df.groupby("department")["salary"].mean()

avg_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[5]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[6]:


print("Employee count by city:")
print(df["city"].value_counts())

print("\nAverage salary by city:")
print(df.groupby("city")["salary"].mean())


# In[7]:


df["salary"].plot(kind="hist", bins=5, edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()


# In[ ]:




