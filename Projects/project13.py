import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
#print("All Visitors: {} ************************************".format(all_visitors))

# how many visitors to the site buy a meal
paying_visitors = noshmishmosh.purchasing_customers
#print("Paying Visitors: {}--------------------------".format(paying_visitors))

total_visitor_count = len(noshmishmosh.customer_visits)
print("Total Visitors: {}".format(total_visitor_count))
paying_visitor_count = len(noshmishmosh.purchasing_customers)
print("Paying Visitors: {}".format(paying_visitor_count))

# determine sample size
baseline_percent = (100 * paying_visitor_count) / total_visitor_count
print("This is the baseline: {0:.2f} %".format(baseline_percent))

# want to confirm we'll bring in at least $1240

amount_needed = 1240
payment_history = noshmishmosh.money_spent
# print(payment_history)

# calculate how many typical purchases to = 1240
average_payment = np.mean(payment_history)
print("Average Payment: $ {0:.2f}".format(average_payment))

# calculate the number of customers needed to reach 1240
new_customer_needed = np.ceil(amount_needed / average_payment)
print("Number of new customers needed: {}".format(new_customer_needed))

# calculate percent lift
percentage_point_increase = 100 * new_customer_needed / total_visitor_count
print("Percent Increase: {} %".format(percentage_point_increase))

minimum_detectable_effect = (percentage_point_increase/baseline_percent) * 100
print("Minimum Detectible Effect: {0:.2f} %".format(minimum_detectable_effect))

statistical_significance = 90

# based on Sample Size Calculator:
ab_sample_size = 280
print("Sample Size: {}".format(ab_sample_size))