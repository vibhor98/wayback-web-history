"""Script to generate stacked bar plot for the increase in different types of MIME per MIME category."""

import math
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alexa-Top-sites.csv')
years = ['1998', '2000', '2005', '2010', '2015', '2021']

year_wise_img_urls = []
# year_wise_text_urls = []
# year_wise_app_urls = []
# year_wise_video_urls = []
# year_wise_audio_urls = []
# year_wise_font_urls = []

for g in df.groupby(['Category']):
    category = g[0]
    if category == 'social networking':
        for year in years:
            image_new_urls = {}
            # text_new_urls = 0
            # app_new_urls = 0
            # video_new_urls = 0
            # audio_new_urls = 0
            # font_new_urls = 0

            for site in g[1]['Site']:
                wayback_df = pd.read_csv('./wayback_crawl_' + year + '/' + site.lower() + '.csv')
                for i in range(len(wayback_df)):
                    row = wayback_df.iloc[i]
                    if row['type'].startswith('video'):
                        image_new_urls[row['type']] = row['new_urls']
                    elif row['type'].startswith('application/x-shockwave'):
                        image_new_urls[row['type']] = row['new_urls']
                        # if row['type'] == 'application/javascript':
                        #     image_new_urls[row['type']] = row['new_urls']
                        # elif row['type'] == 'application/json':
                        #     image_new_urls[row['type']] = row['new_urls']
                        # elif row['type'] == 'application/xml':
                        #     image_new_urls[row['type']] = row['new_urls']
                        # elif row['type'] == 'application/pdf':
                        #     image_new_urls[row['type']] = row['new_urls']
                        # elif row['type'].startswith('application/x-shockwave'):
                        #     image_new_urls[row['type']] = row['new_urls']
                        # else:
                        #     if 'others' not in image_new_urls:
                        #         image_new_urls['others'] = 0
                        #     image_new_urls['others'] += row['new_urls']
                    # elif row['type'].startswith('text'):
                    #     text_new_urls += row['new_urls']
                    # elif row['type'].startswith('application'):
                    #     app_new_urls += row['new_urls']
                    # elif row['type'].startswith('video'):
                    #     video_new_urls += row['new_urls']
                    # elif row['type'].startswith('audio'):
                    #     audio_new_urls += row['new_urls']
                    # elif row['type'].startswith('font'):
                    #     font_new_urls += row['new_urls']

            year_wise_img_urls.append(image_new_urls)
            # year_wise_text_urls.append(text_new_urls)
            # year_wise_app_urls.append(app_new_urls)
            # year_wise_video_urls.append(video_new_urls)
            # year_wise_audio_urls.append(audio_new_urls)
            # year_wise_font_urls.append(font_new_urls)

# year_wise_img_inc = [year_wise_img_urls[0]]
# year_wise_text_inc = [year_wise_text_urls[0]]
# year_wise_app_inc = [year_wise_app_urls[0]]
# year_wise_video_inc = [year_wise_video_urls[0]]
# year_wise_audio_inc = [year_wise_audio_urls[0]]
# year_wise_font_inc = [year_wise_font_urls[0]]
#
# for indx in range(1, len(year_wise_img_urls)):
#     year_wise_img_inc.append(year_wise_img_urls[indx] - year_wise_img_urls[indx-1])
#     year_wise_text_inc.append(year_wise_text_urls[indx] - year_wise_text_urls[indx-1])
#     year_wise_app_inc.append(year_wise_app_urls[indx] - year_wise_app_urls[indx-1])
#     year_wise_video_inc.append(year_wise_video_urls[indx] - year_wise_video_urls[indx-1])
#     year_wise_audio_inc.append(year_wise_audio_urls[indx] - year_wise_audio_urls[indx-1])
#     year_wise_font_inc.append(year_wise_font_urls[indx] - year_wise_font_urls[indx-1])

# print(year_wise_img_urls)
# print(year_wise_text_inc)
# print(year_wise_app_inc)
# print(year_wise_video_inc)
# print(year_wise_audio_inc)
# print(year_wise_font_urls)

# year_wise_img_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_img_inc]
# year_wise_text_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_text_inc]
# year_wise_app_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_app_inc]
# year_wise_video_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_video_inc]
# year_wise_audio_inc = [math.log10(abs(y)) if y!=0 else 0 for y in year_wise_audio_inc]
# year_wise_font_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_font_inc]
img_category_urls = {}

for img_types in year_wise_img_urls[-1]:
    img_category_urls[img_types] = [0]*len(years)

for y in range(len(years)):
    for category in img_category_urls:
        if category in year_wise_img_urls[y]:
            img_category_urls[category][y] = year_wise_img_urls[y][category]

for category in img_category_urls:
    tmp_arr = []
    for i in range(len(years)):
        diff = img_category_urls[category][i]
        # if i == 0 or i == 1:
        #     diff = img_category_urls[category][i]
        # else:
        #     diff = abs(img_category_urls[category][i] - img_category_urls[category][i-1])
        if diff == 0:
            tmp_arr.append(0)
        else:
            tmp_arr.append(math.log10(diff))
    img_category_urls[category] = tmp_arr

print(img_category_urls)
img_sum = [0]*len(years)

categories = list(img_category_urls.keys())

for indx, category in enumerate(img_category_urls):
    if indx > 0:
        img_sum = [sum(x) for x in zip(img_sum, img_category_urls[categories[indx-1]]) ]
        plt.bar(years, img_category_urls[category], bottom=img_sum)
    else:
        plt.bar(years, img_category_urls[category])
# plt.plot(years, year_wise_app_inc, 'go--')
# plt.plot(years, year_wise_video_inc, 'ro--')
# plt.plot(years, year_wise_audio_inc, 'mo--')
# plt.plot(years, year_wise_font_inc, 'yo--')
plt.xlabel('Year')
plt.ylabel('log10 (No. of new URLs of Video MIME-types\n for "Social Networking" category)')
plt.legend(categories)
plt.show()
