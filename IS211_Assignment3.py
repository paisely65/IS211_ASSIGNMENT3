#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment3"""

import urllib2
import argparse
import re
import csv

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Enter the URL to get the CSV file.')
    args = parser.parse_args()
    count = 0
    if args.url:
        try:
            cntx = downloadData(args.url)
            print imgSearch(cntx)
            print browserSearch(cntx)
        except:
            print 'Enter a valid URL'
    else:
        print '--url and then enter url.'


def downloadData(url):
    """fetches the data from url.
    Args:
        response: open url link to get data
        read: reads data
    Return:
        read data file from url"""

    response = urllib2.urlopen(url)
    read = csv.reader(response)
    return read

def imgSearch(url):
    """img percent for the following file"""

    tot = 0
    img = 0
    img_ext = ('.+\.([jpg]|[png]|[jpeg]|[gif]|[JPG]|[PNG]|[JPEG]|[GIF])')
    exp = re.compile(img_ext)
    for row in url:
        filename = row[0]
        tot += 1
        if exp.match(filename):
            img += 1
    img_pct = (float(img) / tot) * 100
    pct = 'Image requests account for {0:0.1f}% of all requests'.format(img_pct)
    return pct


def browserSearch(url):
    """processes the browser with the most hits"""
    fox_cnt = 0
    chrome_cnt = 0
    saf_cnt = 0
    ie_cnt = 0
    fox = ('(|[Firefox]|[firefox])')
    chrome = ('(|[Chrome]|[chrome])')
    saf = ('(|[Safari]|[safari])')
    ie = ('(|[Trident]|[trident])')
    
    for row in url:
        user_agent = row[2]
        if re.search(fox, user_agent):
            fox_cnt += 1
        elif re.search(chrome, user_agent):
            chrome_cnt += 1
        elif re.search(saf, user_agent):
            saf_cnt += 1
        elif re.search(ie, user_agent):
            ie_cnt += 1

    most_hits = max(fox_cnt, chrome_cnt, saf_cnt, ie_cnt)

    if fox_cnt == most_hits:
        return 'Firefox'
    elif saf_cnt == most_hits:
        return 'Safari'
    elif ie_cnt == most_hits:
        return 'Internet Explorer'
    else:
        return 'Chrome'



if __name__ == "__main__":
    main()

