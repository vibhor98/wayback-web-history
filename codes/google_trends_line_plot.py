"""Script to generate line plots from Google Trends data."""

import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('YahooVsGoogle.csv')
#
# fig, ax = plt.subplots(1, 1)
#
# ax.plot(df['Month'], df['Yahoo!'])
# ax.plot(df['Month'], df['Google'])
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.ylabel('Interest over time')
# plt.legend(['Yahoo!', 'Google'])
# ax.set_xticks(ax.get_xticks()[::12])
# plt.show()


# df = pd.read_csv('GeocitiesVsTiktok.csv')
#
# fig, ax = plt.subplots(1, 1)
#
# ax.plot(df['Month'], df['Geocities'])
# ax.plot(df['Month'], df['tiktok'])
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.ylabel('Interest over time')
# plt.legend(['Geocities', 'Tiktok'])
# ax.set_xticks(ax.get_xticks()[::12])
# plt.show()


# df = pd.read_csv('FbVsGoogle.csv')
#
# fig, ax = plt.subplots(1, 1)
#
# ax.plot(df['Month'], df['Facebook'])
# ax.plot(df['Month'], df['Google'])
# plt.xlabel('Year')
# plt.xticks(rotation=90)
# plt.ylabel('Interest over time')
# plt.legend(['Facebook', 'Google'])
# ax.set_xticks(ax.get_xticks()[::12])
# plt.show()


df = pd.read_csv('multiTimeline.csv')

fig, ax = plt.subplots(1, 1)

ax.plot(df['Month'], df['Orkut'], color='r')
ax.plot(df['Month'], df['WhatsApp'], color='g')
ax.plot(df['Month'], df['Instagram'], color='m')
ax.plot(df['Month'], df['Twitter'], color='b')
ax.plot(df['Month'], df['TikTok'], color='k')
plt.xlabel('Year')
plt.xticks(rotation=90)
plt.ylabel('Interest over time')
plt.legend(['Orkut', 'WhatsApp', 'Instagram', 'Twitter', 'TikTok'])
ax.set_xticks(ax.get_xticks()[::12])
plt.show()
