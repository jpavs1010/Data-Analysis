# page visit funnel: analyze data on website visits and describe how many people continue to the next step of the multi
# step process

# describe the following processes:
# user visits to cooltshirts.com
# user adds a t-shirt to the cart
# user clicks "checkout"
# user purchases tshirt

import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
# inspect dataframes:
print(visits.head()) # lists all users who visited website
print(cart.head()) # lists all users who have added t-shirt to cart
print(checkout.head()) # lists all users who have started the checkout
print(purchase.head()) # lists all users who have purchased a t-shirt

cart_visits = pd.merge(visits, cart, how='left')
# new df (cart_visits) will provide all data from visits and only match data from carts: show all users who visited the site and added tshirt to cart
print(cart_visits)

print(len(cart_visits)) #2052 records in cart_visits dataframe

# number of timestamps that are null in column 'cart_time'
null_cart_time = cart_visits[cart_visits.cart_time.isnull()]
print(null_cart_time)

# null rows = visited site but didn't add item to cart (1652 of 2052)

# what percent of users who visited cooltshirts did not place t-shirts in cart
percent_no_item_in_cart = float((len(null_cart_time)/len(cart_visits))*100)
print(len(null_cart_time))
print(len(cart_visits))
print(percent_no_item_in_cart)  # 1652/2052*100 = 80.5

# REDO THIS SECTION >>> find % of users who put items in cart but did not proceed to checkout >>> count null
# values of checkout_time and compare to total number of users who put items in their carts. INSTEAD OF MERGING VISITS
# AND CHECKOUT SHOULD MERGE CART VISITS AND CHECKOUT!!!
# ----------------------------------------------------------------------------------------------------
# cart_checkout = pd.merge(visits, checkout, how='left')
# # new df (cart_checkout) will provide all data from visits and only match data from checkout: show all users
# # who visited the site and went thru checkout
# print(cart_checkout)
# print(len(cart_checkout)) # 2134 records in cart_checkout dataframe
#
# # number of timestamps that are null in column checkout_time
# null_checkout_time = cart_checkout[cart_checkout.checkout_time.isnull()]
# print(null_checkout_time)
# # visited site but didn't check out (1774 of 2134 records in cart_checkout dataframe)
#
# # percent of users who visited site and did not checkout
# percent_no_checkout = float((len(null_checkout_time)/len(cart_checkout))*100)
# print(percent_no_checkout)
# ----------------------------------------------------------------------------------------------------------

cart_checkout = pd.merge(cart_visits, checkout, how='left')
# new df (cart_checkout) will provide all data from cart_visits and only match data from checkout: show all users who
# visited the site and went thru checkout
print(cart_checkout)
print(len(cart_checkout))  # 2254 records in cart_checkout dataframe

# number of timestamps that are null in column checkout_time
null_checkout_time = cart_checkout[cart_checkout.checkout_time.isnull()]
print(null_checkout_time)
# put items in cart but didn't check out (1778 of 2254 records in cart_checkout dataframe)

# percent of users who visited site and did not checkout
percent_no_checkout = float((len(null_checkout_time)/len(cart_checkout))*100)
print(percent_no_checkout)  # = 78.88

# NOT SURE IF THIS IS CORRECT...NOT MAKING LOGICAL SENSE TO ME...LAST DF HAD 2052 RECORDS SO WHEN YOU MERGE CART VISITS
# AND CHECKOUT SHOULD BE AT LEAST THAT MANY RECORDS OR LESS...NEED TO THINK OVER THIS....

# ----------------------------------------------------------------------------------------------------------------------




