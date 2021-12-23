"""Script to generate stacked Bar plot of the number of distinct MIME types."""

import math
import pandas as pd
import matplotlib.pyplot as plt


years = ['1998', '2000', '2005', '2010', '2015', '2021']
year_wise_mime_counts = []

df = pd.read_csv('Alexa-Top-sites.csv')

for y in range(len(years)):
    mime_set = set()
    for site in df['Site']:
        wayback_df = pd.read_csv('./wayback_crawl_' + str(years[y]) + '/' + site.lower() + '.csv')
        for i in range(len(wayback_df)):
            row = wayback_df.iloc[i]
            mime_set.add(row['type'])
    type_wise_mimes = {'text': 0, 'image': 0, 'app': 0, 'others': 0}

    for mime in list(mime_set):
        if mime.startswith('text'):
            type_wise_mimes['text'] += 1
        elif mime.startswith('image'):
            type_wise_mimes['image'] += 1
        elif mime.startswith('app'):
            type_wise_mimes['app'] += 1
        else:
            type_wise_mimes['others'] += 1

    year_wise_mime_counts.append(type_wise_mimes)

print(year_wise_mime_counts)

category_wise_counts = {}
for y in range(len(years)):
    for cat in year_wise_mime_counts[y]:
        if cat not in category_wise_counts:
            category_wise_counts[cat] = [0]*len(years)
        category_wise_counts[cat][y] = year_wise_mime_counts[y][cat]

print(category_wise_counts)

bottom_sum = [0]*len(years)
categories = list(category_wise_counts.keys())

for indx, category in enumerate(category_wise_counts):
    if indx > 0:
        bottom_sum = [sum(x) for x in zip(bottom_sum, category_wise_counts[categories[indx-1]]) ]
        plt.bar(years, category_wise_counts[category], bottom=bottom_sum)
    else:
        plt.bar(years, category_wise_counts[category])

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Number of distinct MIME-types per category', fontsize=10)
plt.legend(list(category_wise_counts.keys()), fontsize=10)
plt.show()

# plt.bar(years, year_wise_mime_counts)
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.xlabel('Year', fontsize=10)
# plt.ylabel('Number of distinct MIME-types', fontsize=10)
# plt.show()
