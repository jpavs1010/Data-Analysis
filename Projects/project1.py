# Unit 1: Sublime Limes
from matplotlib import pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

visits_per_month = [9695, 7909 ,10831, 12942, 12495, 16794,
                    14161, 12762, 12777, 12439, 10309, 8724]

#number of limes of different species sold each month

key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0,
                       79.0, 106.0, 101.0, 103.0, 90.0,
                       102.0, 106.0]

persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0,
                           90.0, 52.0, 63.0, 51.0, 44.0,
                           64.0, 78.0]

blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0,
                         69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

#create a figure with a width = 12 and height = 8
plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1,2,1)
x_values =range(len(months))
plt.plot(x_values, visits_per_month, marker='o')
plt.xlabel('Months')
plt.ylabel('Visits per Month')
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Page Visits per Month')

ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month)
plt.plot(x_values, persian_limes_per_month)
plt.plot(x_values, blood_limes_per_month)
legend_labels = ['Key Limes', 'Persian Limes', 'Blood Limes']
plt.legend(legend_labels)
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.xlabel('Months')
plt.ylabel('Number of Limes Sold')
plt.title('Number of Limes Sold by Month')

plt.subplots_adjust(wspace=.25)

plt.savefig('Page Visits and Limes Sold per Month.png')

plt.show()



plt.show()