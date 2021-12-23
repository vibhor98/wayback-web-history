"""Script to generate MIME-types line plot."""

import math
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alexa-Top-sites.csv')
years = ['1998', '2000', '2005', '2010', '2015', '2021']

year_wise_img_urls = []
year_wise_text_urls = []
year_wise_app_urls = []
year_wise_video_urls = []
year_wise_audio_urls = []
year_wise_font_urls = []

for g in df.groupby(['Category']):
    category = g[0]
    if category == 'travel':
        for year in years:
            image_new_urls = 0
            text_new_urls = 0
            app_new_urls = 0
            video_new_urls = 0
            audio_new_urls = 0
            font_new_urls = 0

            for site in g[1]['Site']:
                wayback_df = pd.read_csv('./wayback_crawl_' + year + '/' + site.lower() + '.csv')
                for i in range(len(wayback_df)):
                    row = wayback_df.iloc[i]
                    if row['type'].startswith('image'):
                        image_new_urls += row['new_urls']
                    elif row['type'].startswith('text'):
                        text_new_urls += row['new_urls']
                    elif row['type'].startswith('application'):
                        app_new_urls += row['new_urls']
                    elif row['type'].startswith('video'):
                        video_new_urls += row['new_urls']
                    elif row['type'].startswith('audio'):
                        audio_new_urls += row['new_urls']
                    elif row['type'].startswith('font'):
                        font_new_urls += row['new_urls']

            year_wise_img_urls.append(image_new_urls)
            year_wise_text_urls.append(text_new_urls)
            year_wise_app_urls.append(app_new_urls)
            year_wise_video_urls.append(video_new_urls)
            year_wise_audio_urls.append(audio_new_urls)
            year_wise_font_urls.append(font_new_urls)

year_wise_img_inc = year_wise_img_urls
year_wise_text_inc = year_wise_text_urls
year_wise_app_inc = year_wise_app_urls
year_wise_video_inc = year_wise_video_urls
year_wise_audio_inc = year_wise_audio_urls
year_wise_font_inc = year_wise_font_urls

# for indx in range(1, len(year_wise_img_urls)):
#     year_wise_img_inc.append(year_wise_img_urls[indx] - year_wise_img_urls[indx-1])
#     year_wise_text_inc.append(year_wise_text_urls[indx] - year_wise_text_urls[indx-1])
#     year_wise_app_inc.append(year_wise_app_urls[indx] - year_wise_app_urls[indx-1])
#     year_wise_video_inc.append(year_wise_video_urls[indx] - year_wise_video_urls[indx-1])
#     year_wise_audio_inc.append(year_wise_audio_urls[indx] - year_wise_audio_urls[indx-1])
#     year_wise_font_inc.append(year_wise_font_urls[indx] - year_wise_font_urls[indx-1])
#
# print(year_wise_img_inc)
# print(year_wise_text_inc)
# print(year_wise_app_inc)
# print(year_wise_video_inc)
# print(year_wise_audio_inc)
# print(year_wise_font_inc)

year_wise_img_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_img_inc]
year_wise_text_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_text_inc]
year_wise_app_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_app_inc]
year_wise_video_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_video_inc]
year_wise_audio_inc = [math.log10(abs(y)) if y!=0 else 0 for y in year_wise_audio_inc]
year_wise_font_inc = [math.log10(y) if y!=0 else 0 for y in year_wise_font_inc]


plt.plot(years, year_wise_img_inc, 'bo--')
plt.plot(years, year_wise_text_inc, 'ko--')
plt.plot(years, year_wise_app_inc, 'go--')
plt.plot(years, year_wise_video_inc, 'ro--')
plt.plot(years, year_wise_audio_inc, 'mo--')
plt.plot(years, year_wise_font_inc, 'yo--')
plt.xlabel('Year')
plt.ylabel('log10 (No. of new URLs for different MIME-types\n for "Travel" category)')
plt.legend(['Image', 'Text', 'Application', 'Video', 'Audio', 'Font'])
plt.show()
