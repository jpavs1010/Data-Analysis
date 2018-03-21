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
print('Visits: {}'.format(visits.head()))  # lists all users who visited website
print('Cart: {}'.format(cart.head()))  # lists all users who have added t-shirt to cart
print('Checkout: {}'.format(checkout.head()))  # lists all users who have started the checkout
print('Purchase: {}'.format(purchase.head()))  # lists all users who have purchased a t-shirt

cart_visits = pd.merge(visits, cart, how='left')
# new df (cart_visits) will provide all data from visits and only match data from carts: show all users who visited the site and added tshirt to cart
print('Cart Visits: {}'.format(cart_visits))

print('Number records in Cart Visits: {}'.format(len(cart_visits)))  # 2052 records in cart_visits dataframe

# number of timestamps that are null in column 'cart_time'
null_cart_time = cart_visits[cart_visits.cart_time.isnull()]
print('Number of timestamps that are null in column cart_time {}'.format(null_cart_time))

# null rows = visited site but didn't add item to cart (1652 of 2052)

# what percent of users who visited cooltshirts did not place t-shirts in cart
percent_no_item_in_cart = float((len(null_cart_time) / len(cart_visits)) * 100)
print(len(null_cart_time))
print(len(cart_visits))
print('Percent of users who visited and did not place item in cart: {}'.format(percent_no_item_in_cart))
# 1652/2052*100 = 80.5

# merge cart and checkout and count null values
cart_checkout = pd.merge(cart, checkout, how='left')
print('Cart Checkout {}'.format(cart_checkout))
print('Number of records in cart checkout {}'.format(len(cart_checkout)))  # 602 records in cart_checkout dataframe

# count null values of checkout_time
null_checkout_time = cart_checkout[cart_checkout.checkout_time.isnull()]
print('Count null values of checkout time: {}'.format(null_checkout_time))
# 126 records with null value

# percentage of users put item in cart but did not proceed to check out
percent_item_cart_no_checkout = float((len(null_checkout_time) / len(cart_checkout)) * 100)
print('Percent of users put item in cart but did not proceed to checkout: {}'.format(percent_item_cart_no_checkout))
# 20.93%

# merge all four steps of the funnel, in order using series of left merges
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print('all data: {}'.format(all_data))

# percent of users proceeded to checkout but didn't purchase a t-shirt:
# count number of records in all data
print('Number of records in all data: {}'.format(len(all_data)))
# 2594 records

# count occurrences of null in purchase_time
null_purchases = all_data[all_data.purchase_time.isnull()]
print('Count null values of purchase time: {}'.format(len(null_purchases)))
# 1898 records

percent_to_checkout_no_purchase = float((len(null_purchases) / len(all_data)) * 100)
print('Percent of users proceeded to checkout without a purchase: {} %'.format(percent_to_checkout_no_purchase))
# 73.168 %

# which step of the funnel is the weakest--the highest percentage of users not completing it?
print('The weakest part of the funnel is the visit to cart transition as 80.5% of visitors to the site do not place an item in the cart. Cool T-Shirts Inc could make changes to their site to fix this problem by reviewing what information is provided on the site. Maybe the customer requires more information before submitting add to cart, for example maybe they require knowing if it is same day delievery, the price, or whether or not a coupon can be applied before they even bother clicking add to cart.')

# Average Time to Purchase
# calculate the average time from initial visit to final purchase

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
# this will add the time to purchase column to df

print(all_data.time_to_purchase)

# average time to purchase
print('Average Time to Purchase: {}'.format(all_data.time_to_purchase.mean()))