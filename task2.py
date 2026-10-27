# Functions and Comprehensions

prices = [500,1200,800,2500,300]

#create apply discount

def apply_discount(price,discount=10):
    discount_amount = price * discount/100
    final_price = price - discount_amount
    return final_price

print("apply_discount(1000) --> ",apply_discount(1000))
print("apply_discount(1000,25) --> ",apply_discount(1000,25))

# create total(*args)

def total(*args):
    return sum(args) 

print("total(5,10,15) --> ",total(5,10,15))

# create describe(**Kwargs)

def describe(**kwargs):
    for key,value in kwargs.items(): 
        print(key,":",value)

print("\nProduct details: " )
describe(product="Laptop",price=45000,quantity=2)

#list comprehension

above_1000 = [price for price in prices if price > 1000]
print("\nAbove 1000:",above_1000)

# use map() with lambda

gst = list(map(lambda price : round(price*1.18,2),prices))
print("With Gst:",gst)

#filter()

below_1000 = list(filter(lambda price : price < 1000 , prices))
print("Below 1000: ",below_1000)

