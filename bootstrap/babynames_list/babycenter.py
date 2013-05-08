#!/usr/bin/env python
"""Scrape the web a little for an initial list of baby names.
"""
from lxml.html import parse

TOP_URL = 'http://www.babycenter.com/baby-names-ideas'

def main():
    "The entry point"
    root = parse(TOP_URL).getroot()
    for div in root.cssselect('div.centerColInner a'):
        div.make_links_absolute(TOP_URL, resolve_base_href=True)
        for anchor in div.cssselect('a'):
            sub_url = anchor.attrib.get('href')
            sub_root = parse(sub_url).getroot()
            for list_item in sub_root.cssselect('ul.babynames li'):
                print list_item.text_content().encode('utf8')


if __name__ == '__main__':
    exit(main())
