## Merging Datasets

import pandas as pd

orders=pd.read_csv("orders.csv")
orders=orders.drop_duplicates()

customers=pd.read_csv("customers.csv")

merge=pd.merge(orders,customers,on="customer_id",how="inner")

# Find customer IDs that are missing from customers.csv
dropped=orders[~orders["customer_id"].isin(customers["customer_id"])]
print(f"Inner join rows: {len(merge)} (customer {dropped["customer_id"].iloc[0]} dropped)")

left=customers.merge(orders,on="customer_id",how="left")

no_orders = left[left["order_id"].isna()]
print("No orders: ",",".join(no_orders["name"]))

outer=pd.merge(orders,customers,on="customer_id",how="outer",indicator=True)
# indicator it create a extra column _merge
no_Customer =outer[outer["_merge"]=="left_only"]

print("Order without customer: ",",".join(no_Customer["customer_id"].astype(str)))




