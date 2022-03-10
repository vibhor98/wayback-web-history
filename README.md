# "Way back then": A Data-driven View of 25+ years of Web Evolution
Vibhor Agarwal and Nishanth Sastry, "Way back then": A Data-driven View of 25+ years of Web Evolution, The Web Conference (WebConf), 2022.

## Abstract
Since the inception of the first web page three decades back, the Web
has evolved considerably, from static HTML pages in the beginning
to the dynamic web pages of today, from text-only to more towards
multimedia, etc. Although much of this is known anecdotally, to our
knowledge, there is no quantitative documentation of the extent
and timing of these changes. This paper attempts to address this
gap in the literature by looking at the top 100 Alexa websites for
over 25 years from the Internet Archive or the “Wayback Machine”,
*archive.org*. We study the changes in popularity, from Geocities
and Yahoo! in the mid-to-late 1990s to the likes of Google, Facebook,
and Tiktok of today. We also look at different categories of
websites and their popularity over the years, the emergence and
relative prevalence of different mime-types (text vs. image vs. video
vs. javascript and json) and study whether the use of text on the
Internet is declining.

The paper PDF is available [here](https://arxiv.org/pdf/2202.08239.pdf)!

## Directory Structure
* `codes` folder contains scraper for *archive.org* and other Python scripts used for analysis.
* `figures` folder contains all the figures used in the WebConf paper.
* `google_trends_data` folder contains the datasets downloaded from Google Trends.
* `wayback_datasets` folder contains the data crawled from *archive.org*.
* `year_wise_top_websites` folder contains the year-wise top 10 websites.
* `Alexa-Top-sites.csv` contains top 100 websites collected from *Alexa.com* based on Alexa rankings in Nov 2021.

## Citation
If you find this paper useful in your research, please consider citing:
```
@inproceedings{agarwal2022waybackthen,
title={"Way back then": A Data-driven View of 25+ years of Web Evolution},
author={Vibhor Agarwal and Nishanth Sastry},
booktitle={The Web Conference (WebConf)},
year={2022}
}
```
