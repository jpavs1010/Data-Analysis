# Unit 3 Betty's Bakery: numpy project

import numpy as np

# all recipes contain: flour, sugar, eggs, milk, butter
# data in cups
cupcakes = np.array([2, .75, 2, 1, .5])

# recipes in csv pull in data:
recipes = np.genfromtxt('recipes.csv', delimiter=',')

print(recipes)
# row1 = cupcakes, row2 = pancakes, row3 = cookie, row4 = bread

# 3rd column is the number of eggs for each recipe
# select all elements from the 3rd column
eggs = recipes[:,2]

# which recipe requires exactly 1 egg?
print(eggs == 1)

# 2 batches of cupcakes, 1 batch of cookies
double_batch = cupcakes * 2
print(double_batch)

cookies = recipes[2,:]
print(cookies)

grocery_list = cookies + double_batch
print(grocery_list)

