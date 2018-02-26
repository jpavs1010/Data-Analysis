# FetchMaker: match prospective dog owners with perfect pet

import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from matplotlib import pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

# ____________________________________________________________________________________________________________________


def pval_significance(pval):
    if pval < 0.05:
        print("Reject Null Hypothesis")
    else:
        print("Accept Null Hypothesis")
# ______________________________________________________________________________________________________________________

# ---------------------------------------------------------------------------------------------------------------------
# tail lengths of all the rottweiler's
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print("Rottweiler tail length data: {}".format(rottweiler_tl))

mean_rottweiler_tl = np.mean(rottweiler_tl)
std_rottweiler_tl = np.std(rottweiler_tl)
print("Rottweiler Mean: {}".format(mean_rottweiler_tl))
print("Rottweiler Standard Deviation: {}".format(std_rottweiler_tl))

# ---------------------------------------------------------------------------------------------------------------------

# expect 8% of dogs in FetchMaker system to be rescues
expected_pct_rescues = 0.08
# want to know if whippets are significantly more or less likely to be a rescue

# obtain the number of whippets that are rescues
whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescue = np.count_nonzero(whippet_rescue)
print("Number of Whippets Rescued: {}".format(num_whippet_rescue))  # 6 whippets are rescues

# get the number of samples in whippet set
num_whippets = np.size(whippet_rescue)
print("Sample Size of Whippets: {}".format(num_whippets))  # 100 whippets in sample

# binomial test
pval_whippets_rescued = binom_test(num_whippet_rescue, n=num_whippets, p=expected_pct_rescues)

print("Significance Level Whippets Rescued: {}".format(pval_whippets_rescued))
print(pval_significance(pval_whippets_rescued))
# pval = 0.58117 > 0.05 result is not significant: therefore we accept the null hypothesis: unlikely that the sample
# of whippets are rescue dogs

# ---------------------------------------------------------------------------------------------------------------------

# most popular mid-sized dog breeds whippets, terriers, pitbulls. Is there a significant difference in the average
# weights of the 3 dog breeds?

# use ANOVA statistical analysis for 2+ numerical data sets

# assumptions of numerical hypothesis tests:
# 1. samples are normally distributed
# 2. population st.dev. is equal
# 3. samples are independent

# get weight of each dog breed
weight_whippet = fetchmaker.get_weight("whippet")
weight_terrier = fetchmaker.get_weight("terrier")
weight_pitbull = fetchmaker.get_weight("pitbull")

# check for approx normal distribution:
plt.hist(weight_whippet)
plt.show()

plt.hist(weight_terrier)
plt.show()

plt.hist(weight_pitbull)
plt.show()

# each are approximately normally distributed

# check for st.dev is equal:
ratio_whippet_terrier_stdev = np.std(weight_whippet) / np.std(weight_terrier)
ratio_whippet_pitbull_stdev = np.std(weight_whippet) / np.std(weight_pitbull)
ratio_terrier_pitbull_stdev = np.std(weight_terrier) / np.std(weight_pitbull)

print("Standard Deviation Ratio (whippet/terrier): {}".format(ratio_whippet_terrier_stdev))
print("Standard Deviation Ratio (whippet/pitbull): {}".format(ratio_whippet_pitbull_stdev))
print("Standard Deviation Ratio (terrier/pitbull): {}".format(ratio_terrier_pitbull_stdev))
# ratios are approximately close to 1

# samples of weight of each breed do no affect the values of another therefore are independent from each other

# anova: Is there a significant difference in the average weights of the 3 dog breeds?
fstat, pval_weight_breeds = f_oneway(weight_whippet, weight_terrier, weight_pitbull)

print("P-Value for Dog Breed Weights (whippet, terrier, pitbull): {}".format(pval_weight_breeds))
print(pval_significance(pval_weight_breeds))

# pval = 3.27 e-17 < 0.05, is significant. Therefore, we reject the null hypothesis: we are reasonably confident
# that there is a pair of the data sets that have a significant difference in the average weights of the 3 dog breeds

# to find out which two data sets are significantly different use tukey range test

all_breeds = np.concatenate([weight_whippet, weight_terrier, weight_pitbull])

labels = ['whippet'] * len(weight_whippet) + ['terrier'] * len(weight_terrier) + ['pitbull'] * len(weight_pitbull)

breed_tukey = pairwise_tukeyhsd(all_breeds, labels, 0.05)
print(breed_tukey)
# reject null hypothesis for pitbull/terrier and terrier/whippet:
# 1. reasonably confident that the pitbull and terrier data sets have a significant difference in the average weight
# between the two breeds
# 2. reasonably confident that the terrier and whippet data sets have a significant difference in the average weight
# between the two breeds.

# accept null hypothesis for pitbull/whippet:
# 1. pitbull and whippet data sets do not have a significant difference in the average weight between the two breeds

# ---------------------------------------------------------------------------------------------------------------------

# let's see if poodle's and shitzu's have significantly different colors

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")
print("Data on Poodle Colors: {}".format(poodle_colors))
print("Data on Shihtzu Colors: {}".format(shihtzu_colors))

# get the number of occurrences of each poodle color
black_poodle = np.count_nonzero(poodle_colors == "black")
brown_poodle = np.count_nonzero(poodle_colors == "brown")
gold_poodle = np.count_nonzero(poodle_colors == "gold")
grey_poodle = np.count_nonzero(poodle_colors == "grey")
white_poodle = np.count_nonzero(poodle_colors == "white")

poodle = [black_poodle, brown_poodle, gold_poodle, grey_poodle, white_poodle]
print("Poodle Color List(black, brown, gold, grey, white): {}".format(poodle))

# get the number of occurrences of each shihtzu color
black_shihtzu = np.count_nonzero(shihtzu_colors == "black")
brown_shihtzu = np.count_nonzero(shihtzu_colors == "brown")
gold_shihtzu = np.count_nonzero(shihtzu_colors == "gold")
grey_shihtzu = np.count_nonzero(shihtzu_colors == "grey")
white_shihtzu = np.count_nonzero(shihtzu_colors == "white")

shihtzu = [black_shihtzu, brown_shihtzu, gold_shihtzu, grey_shihtzu, white_shihtzu]
print("Shihtzu Color List(black, brown, gold, grey, white): {}".format(shihtzu))


def merge(list1, list2):
    table = []
    for i in range(len(list1)):
        table.append([list1[i], list2[i]])
    return table

color_table = merge(poodle, shihtzu)
print("Merged Poodle and Shihtzu Color Count(black, brown, gold, grey, white): {}".format(color_table))

chi2, pval_color_table, dof, expected = chi2_contingency(color_table)
print("P-Value for Chi Square Test: {}".format(pval_color_table))
print(pval_significance(pval_color_table))
# p-value = 0.005302 < 0.05: indicates a significant difference; we reject the null hypothesis
# poodle's and shihtzu's do have a significant difference in color
