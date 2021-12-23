"""Script to generate Bar plots."""

import math
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alexa-Top-sites.csv')
# df['Category'].value_counts().plot.bar()
# plt.xlabel('Website Category')
# plt.ylabel('Number of Websites')

# df.groupby(['Category'])['Daily Pageviews per Visitor'].median().sort_values(ascending=False).plot.bar()
# plt.xlabel('Website Category')
# plt.ylabel('Median Daily Pageviews per Visitor')

def convert_to_mints(x):
    mints, secs = x.split(':')
    mints = int(mints) + int(secs) / 60
    return mints

df['Daily Time in mints'] = df['Daily Time on Site'].apply(lambda x: convert_to_mints(x))

print(df['Daily Time in mints'].sum())
print(df['Daily Time in mints'].head(10).sum())

# df.groupby(['Category'])['Daily Time in mints'].sum().sort_values(ascending=False).plot.bar()
# plt.xlabel('Website Category')
# plt.ylabel('Average Daily Time on Site\nper Visitor (in mints.)')
#
# plt.show()

# t = {}
#
# for g in df.groupby(['Category']):
#     category = g[0]
#     image_new_urls = 0
#     num_sites = 0
#     for site in g[1]['Site']:
#         num_sites += 1
#         wayback_df = pd.read_csv('./wayback_crawl_2021/' + site.lower() + '.csv')
#         for i in range(len(wayback_df)):
#             row = wayback_df.iloc[i]
#             if row['type'].startswith('application'):
#                 image_new_urls += row['new_urls']
#     t[category] = image_new_urls / num_sites
#
# # del t['search engine']
# # del t['social networking']
#
# # log y-axis
# t = {k: math.log10(v) for k, v in t.items()}
#
# sorted_t = {k: v for k, v in sorted(t.items(), key=lambda item: item[1], reverse=True)}
#
# plt.bar(x=list(sorted_t.keys()), height=list(sorted_t.values()))
# plt.xlabel('Website Category')
# plt.xticks(rotation=90)
# plt.ylabel('log10 (total no. of new Application URLs)')
# plt.show()
