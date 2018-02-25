# Familiar: A Study in Data Analysis
# Familiar startup in the new market of blood transfusion; looking for insights about product


import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

vein_pack_lifespans = familiar.lifespans('vein')
# print(vein_pack_lifespans)

# looking to see if subscribers to the Vein Pack live longer than others; is the average lifespan of Vein Pack
# subscriber significantly different from average life expectancy of 71 years?

tstat, pval = ttest_1samp(vein_pack_lifespans, 71)
print(
    pval)  # pval < 0.05: reject null hypothesis, the average lifespan of vein pack subscriber is significantly
# different from average life expectancy


def pval_significance(pval):
    if pval < 0.05:
        print("The Vein Pack is Proven to Make You Live Longer!")
    else:
        print("The Vein Pack Is Probably Good For You Somehow!")


pval_significance(pval)

# compare lifespan data between different packages(compare Vein Pack and Artery Pack)
artery_pack_lifespans = familiar.lifespans('artery')
# print(artery_pack_lifespans)

# see if subsribers to Artery Pack experience a significant improvement beyond what a Vein Pack subscriber benefits?
# use 2 sample t-test to compare

package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results)


def comparison_pval(package_comparison_results):
    if package_comparison_results.pvalue < 0.05:
        print("the Artery Package guarantees even stronger results")
    else:
        print("the Artery Package is also a great product")


print(comparison_pval(package_comparison_results))
# the pvalue is greater than 0.05: reject null hypothesis: there is not a significant improvement for Artery Pack
#  users beyond what a Vein Pack subscriber benefits (not statisically significant)

# demonstrate the benefits of the artery package compared to the average lifespan
artery_pval = ttest_1samp(artery_pack_lifespans, 71)
print(artery_pval)


def pval_significance(artery_pval):
    if artery_pval.pvalue < 0.05:
        print("The Artery Pack is Proven to Make You Live Longer!")
    else:
        print("The Artery Pack Is Probably Good For You Somehow!")


print(pval_significance(artery_pval))
# Artery pack could improve lifespan, but not significantly better than vein pack

# other benefits of artery package: compare iron counts between packages: use iron counts from familiar.py

iron_contingency_table = familiar.iron_counts_for_package()

print(iron_contingency_table)

# is there a significant difference between artery package subscribers iron levels vs vein package subscribers? use
# chi-square test

chi2, iron_pvalue, dof, expected = chi2_contingency(iron_contingency_table)
print(iron_pvalue)


def chi2_pval_significance(iron_pvalue):
    if iron_pvalue < 0.05:
        print("The Artery Package is Proven to Make you Healthier!")
    else:
        print("While We Can't Say The Artery Package Will Help You,I Bet It's Nice!")


print(chi2_pval_significance(iron_pvalue))

# "with proven benefits to both of the product lines, we can ramp up marketing and sales!"

