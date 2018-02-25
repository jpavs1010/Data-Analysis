# Unit 2: A/B Testing
import pandas as pd

# A-B Testing: Analyze Ad Clicks
ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

views = ad_clicks.groupby('utm_source').count()

#print(views)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()


clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

#print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()

#print(clicks_pivot)


clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) * 100

#print(clicks_pivot)
# -------------------------------------
#Analyze A/B Test
views_by_group = ad_clicks.groupby('experimental_group').count()
#print(views_by_group)
#827 people were shown group a, 827 people shown group b.

views_group_and_click = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
#print(views_group_and_click)

views_pivot = views_group_and_click.pivot (columns='experimental_group', index='is_click', values='user_id').reset_index()

#print(views_pivot)

#OR prefer pivot 2
views_pivot2 = views_group_and_click.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()

#print(views_pivot2) #more people chose site A over site B question is...is it a significant difference?

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
#print(a_clicks.head())
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
#print(b_clicks.head())

a_click_by_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
#print(a_click_by_day)

b_click_by_day = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
#print(b_click_by_day)

a_pivot = a_click_by_day.pivot(columns='day', index='is_click', values='user_id').reset_index()
print(a_pivot)

b_pivot = b_click_by_day.pivot(columns='day', index='is_click', values='user_id').reset_index()

print(b_pivot)

#recommend using site a; however are these findings statistically significant? maybe we should look at that too?