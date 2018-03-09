# Bayes Theorem allows us to incorporate prior knowledge into probability calculations
# How likely is it that a student understands the material given that they know the correct answer?

# probability of a given b where:
a = 'knows material'
b = 'answered correctly'
# p(a|b) = probability that student knows material given student answered correctly
print('p(a|b): The probability that {} given {} will be represented as p(k|c)'.format(a,b))

# #assumption:
p_knows_material = .60
print('p(k): {}'.format(p_knows_material))
p_doesnt_know_material = 1-.60
print('p(non-k): {}'.format(p_doesnt_know_material))

# assumption:
p_wrong_answ_given_knows_material = .15
# p(non-c|k) = .15
# p(c|k) = 1-.15
p_correct_answ_given_knows_material = 1-.15
print('p(c|k): {}'.format(p_correct_answ_given_knows_material))
print('p(non-c|k): {}'.format(p_wrong_answ_given_knows_material))

# assumption:
p_correct_answ_given_doesnt_know_material = .20
# p(c|non-k) = .20
print('p(c|non-k): {}'.format(p_correct_answ_given_doesnt_know_material))

# p(c) = probability of answering correctly is: calculate weighted average
#      = p(c|k) * p(k) + p(c|non-k) * p(non-k)
#      = p(c|k) *.60 + p(c|non-k) * 1-.60
#      = 1-.15 * .60 + .20 * 1-.60
p_correct_answ = p_correct_answ_given_knows_material * p_knows_material + p_correct_answ_given_doesnt_know_material * \
                                                                          p_doesnt_know_material
print('p(c): {}'.format(p_correct_answ))

# Bayes Theorem:
# p(a|b) = p(b|a) * p(a) / p(b)

# p(k|c) = p(c|k) * p(k) / p(c)
p_knows_material_given_correct_answ = p_correct_answ_given_knows_material * p_knows_material / p_correct_answ
print('p(k|c): {}'.format(p_knows_material_given_correct_answ))

print('It is likely that the student knows the material when they give the correct answer {} % of the time'
      .format(round(p_knows_material_given_correct_answ*100)))
