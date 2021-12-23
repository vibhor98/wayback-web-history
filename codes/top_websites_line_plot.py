"""Script to generate stacked bar plot for % of visits per website category."""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

years = ['1995', '1998', '2000', '2005', '2010', '2015', '2021']

year_wise_category_counts = []
year_wise_category_counts_with_search = []

# for y in range(len(years)):
#     df = pd.read_csv('./year_wise_top_websites/websites_' + str(years[y]) + '.csv')
#     category_dict = dict(Counter(df['category']))
#     for category in category_dict:
#         if category not in year_wise_category_counts:
#             year_wise_category_counts[category] = [0]*len(years)
#         year_wise_category_counts[category][y] = category_dict[category]


for y in range(len(years)):
    df = pd.read_csv('./year_wise_top_websites/websites_' + str(years[y]) + '.csv')
    df = df.groupby('category')['visits'].sum()
    cat_df = dict(df)
    cat_df_old = dict(df)
    del cat_df['search engine']

    # normalize
    print(cat_df)
    deno = sum(list(cat_df.values()))
    for category in cat_df:
        cat_df[category] = (cat_df[category] / deno) * 100

    deno = sum(list(cat_df_old.values()))
    for category in cat_df_old:
        cat_df_old[category] = (cat_df_old[category] / deno) * 100

    year_wise_category_counts.append(cat_df)
    year_wise_category_counts_with_search.append(cat_df_old)


print(year_wise_category_counts)

category_wise_counts = {}
category_wise_counts_with_search = {}
for y in range(len(years)):
    for cat in year_wise_category_counts[y]:
        if cat not in category_wise_counts:
            category_wise_counts[cat] = [0]*len(years)
        category_wise_counts[cat][y] = year_wise_category_counts[y][cat]
    for cat in year_wise_category_counts_with_search[y]:
        if cat not in category_wise_counts_with_search:
            category_wise_counts_with_search[cat] = [0]*len(years)
        category_wise_counts_with_search[cat][y] = year_wise_category_counts_with_search[y][cat]

print(category_wise_counts)


# for indx, category in enumerate(year_wise_category_counts):
#     plt.plot(years, year_wise_category_counts[category])
fig = plt.figure()
ax = plt.subplot(111)

bottom_sum = [0]*len(years)
categories = list(category_wise_counts.keys())

for indx, category in enumerate(category_wise_counts):
    if indx > 0:
        bottom_sum = [sum(x) for x in zip(bottom_sum, category_wise_counts[categories[indx-1]]) ]
        plt.bar(years, category_wise_counts[category], bottom=bottom_sum)
    else:
        plt.bar(years, category_wise_counts[category])


plt.plot(category_wise_counts_with_search['search engine'], marker='o')

plt.xlabel('Year', fontsize=10)
plt.ylabel('Percentage of Visits', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

cat_list = list(category_wise_counts.keys())
cat_list.insert(0, 'search engine')

ax.legend(cat_list, loc='upper center', bbox_to_anchor=(0.5, 1.23),
          ncol=3, fancybox=True, shadow=False, fontsize=10)
plt.show()
