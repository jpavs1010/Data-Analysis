# Unit 3: Candidate Surveys
# Election Results

import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# calculate the number of people that responded ceballos
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print(total_ceballos)

# calculate the % of people in the survey who votes Ceballos
total = sum([1 for n in survey_responses])
print(total)
percentage_ceballos = (total_ceballos / total)
print(percentage_ceballos)

# in election 54% voted Ceballos population = 10,000
# poll predicted very different outcome
# generate binomial distribution, see if something is wrong witht the poll, or given sample size it was a reasonable
# result
possible_surveys = np.random.binomial(total, .54, size=10000) / float(total)
print(possible_surveys)

# plot histogram
plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()

# 47% surveyed said would vote for Ceballos but 54% voted for Ceballos, what's the % of surveys that could have an
# outcome of Ceballos receiving less than 50% of the vote?
ceballos_loss_surveys = np.mean(possible_surveys < .50)
print(ceballos_loss_surveys)

# current poll = 20% of the time a survey output would predict Kerrigan winning even if Ceballos won the actual election
# poll would be more accurate with more responders
large_survey = np.random.binomial(7000, .54, size=10000) / float(7000)
print(large_survey)
ceballos_loss_new = np.mean(large_survey < .50)
print(ceballos_loss_new)

# new value is 0; prediciting results from survey it is important to take into consideration the size of the poll for
# increased accuracy
