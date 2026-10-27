# sales report basics
# Create variables of every type 
count=0
sales_amount = 18000
discount_amount = 99.9
product_name = "Mobile"
sales_list=[12000,0,8500,15000,-200,9800]
product_details = {product_name:"Mobile", sales_amount : 18000,"count":2}
product_ids = {101,102,103}
sales_days = ("Monday","Wednesday","Friday")

# print values and its type

print(sales_amount,type(sales_amount))
print(discount_amount,type(discount_amount))
print(product_name,type(product_name))
print(sales_list,type(sales_list))
print(product_details,type(product_details))
print(product_ids,type(product_ids))
print(sales_days,type(sales_days))


total=0

for value in sales_list:
    if value <=0:
        print("Skipped invalid value ",value)
        continue

    total=total+value
    print("Added", value,"total", total)

    if total > 30000:
        break

if total > 30000:
    print("Target reached. Stopped at", total)
elif total == 30000:
    print("Target exactly reached")
else:
    print("Target not reached")
