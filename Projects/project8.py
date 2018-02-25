# Unit 3: Statistics with Cereal
# nutritional data from several competitors
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

average_calories = np.mean(calorie_stats)
print(average_calories) # 106 as compared to crunchiemunchies brand is 60 calories

# does the average reflect the distribution of the dataset: sort data

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted) # range of calories 50 to 160: majority of cereals are higher than the mean

median_calories = np.median(calorie_stats)
print(median_calories) # 110 vs 106 mean

# median demonstrates at least half the values are over 100 calories, lets see if there is a significant portion of
# the competition is higher than crunchiemuchies 60 calories

nth_percentile = np.percentile(calorie_stats, 4)
print(nth_percentile) # lowest percentile that is greater than 60 calories: 4%  is equal to or less than 70 calories

# the majority of the competition has a much higher calorie count. let's calculate the percentage of cereals that have
# more than 60 calories per serving

more_calories = np.mean(calorie_stats > 60)*100
print(more_calories) # 96%

# how much variation exists in the dataset? can we generalize that most cereals have around 100 calories or is the
# spread even greater?
calorie_std = np.std(calorie_stats)
print(calorie_std) # 19.35 what does us tell us if we don't have a comparison dataset? 19 is a fairly low number and the
#  lower the standard deviation the less spread out the data...

# overall the majority of CrunchieMunchies competitors have a higher calorie content. That insight is a competitive edge
#  that CrunchieMunchies should draw attention to in future marketing; though we should also look more deeply into the
# competitors who have similar calorie content so we can be sure to call out our edge against them.





