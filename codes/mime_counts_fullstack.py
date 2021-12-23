"""Script to generate full-stack Bar plots for different MIME-types (images, videos, etc.)."""

import math
import pandas as pd
import matplotlib.pyplot as plt


years = ['1998', '2000', '2005', '2010', '2015', '2021']
year_wise_mime_counts = []

df = pd.read_csv('Alexa-Top-sites.csv')

for y in range(len(years)):
    mime_dict = {}
    for site in df['Site']:
        wayback_df = pd.read_csv('./wayback_crawl_' + str(years[y]) + '/' + site.lower() + '.csv')
        for i in range(len(wayback_df)):
            row = wayback_df.iloc[i]
            if row['type'].startswith('image'):
                if 'image' in mime_dict:
                    mime_dict['image'] += row['new_urls']
                else:
                    mime_dict['image'] = row['new_urls']
            elif row['type'].startswith('text'):
                if 'text' in mime_dict:
                    mime_dict['text'] += row['new_urls']
                else:
                    mime_dict['text'] = row['new_urls']
            elif row['type'].startswith('app'):
                if 'app' in mime_dict:
                    mime_dict['app'] += row['new_urls']
                else:
                    mime_dict['app'] = row['new_urls']
            else:
                if 'others' in mime_dict:
                    mime_dict['others'] += row['new_urls']
                else:
                    mime_dict['others'] = row['new_urls']

    for k in mime_dict:
        mime_dict[k] = math.log10(mime_dict[k])

    deno = sum(list(mime_dict.values()))
    for category in mime_dict:
        mime_dict[category] = (mime_dict[category] / deno) * 100
    year_wise_mime_counts.append(mime_dict)

# Find %increase
# for y in range(1, len(years)):
#     for cat in year_wise_mime_counts[y]:
#         year_wise_mime_counts[y][cat] = abs(year_wise_mime_counts[y][cat] - year_wise_mime_counts[y-1][cat])

print(year_wise_mime_counts)

category_wise_counts = {}
for y in range(len(years)):
    # deno = sum(list(year_wise_mime_counts[y].values()))
    # for category in year_wise_mime_counts[y]:
    #     # year_wise_mime_counts[y][category] = (year_wise_mime_counts[y][category] / deno) * 100
    #     year_wise_mime_counts[y][category] = math.log10(year_wise_mime_counts[y][category])

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
plt.ylabel('Percentage of number of new URLs for different MIME-types', fontsize=10)
plt.legend(list(category_wise_counts.keys()), fontsize=10)
plt.show()
