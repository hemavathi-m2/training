## cleaning and Aggregation

import pandas as pd

df = pd.read_csv("orders.csv")

#Find missing values
missing=df.isna().sum().sum()
duplicate=df.duplicated().sum()

print("Missing: amount ",missing," | Duplicates: ",duplicate)

# drop duplicates
df=df.drop_duplicates()

#Fill missing amount with median 
median_value= df["amount"].median()
df["amount"]=df["amount"].fillna(median_value)
print("Median used: ",median_value)

#type conversion

df["amount"]=pd.to_numeric(df["amount"],errors="coerce")
df["order_id"]=df["order_id"].astype(str)

#groupby and agg
final=df.groupby("customer_id").agg(total=("amount","sum"),orders=("order_id","count"))
print(final)




