# -*- coding: utf-8 -*-
import requests
import urllib2
from bs4 import BeautifulSoup
from datetime import timedelta
import json

def goal_com(current, end):
    page_link = []
    td = timedelta(days=+1)  # time delta value.
    while current < end:
        # Get page url  to json url
        url = 'http://www.goal.com/kr/results/' + str(current) + '/8?ICID=RE_CAL_1'
        soup = link_connect(url)
        link_page = soup.find("table", {"data-competition-id": "8"})
        try:
            find_dat = link_page.find("a", {"class": "btn match-btn"})
        except AttributeError:
            current += td
            pass
        else:
            if find_dat != None:
                for epl in link_page.find_all("a", {"class": "btn match-btn"}):
                    href = epl.get('href')  # link 접속후 데이터 추출.
                    page_url = 'http://www.goal.com/' + str(href)

                    # Stats Page Url
                    page_soup = link_connect(page_url)
                    stats_page = page_soup.find("li", {"class": "stats "})
                    stats_href = stats_page.find_next("a").get('href')
                    stats_page_url = 'http://www.goal.com/' + str(stats_href)
                    stats_page_soup = link_connect(stats_page_url)

                    # Json url
                    team_dat_header = stats_page_soup.find("div", {"class": "main-content stats"})
                    header = team_dat_header.find('article')
                    json_url = header.get('data-opta-match-id')
                    page_link.append(json_url)
                current += td
                print current
    return page_link


def link_connect(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    return soup

def get_data(url):
    json_url = 'http://www.goal.com/feed/matches/statistics?optaMatchId=' + str(url)
    a = urllib2.urlopen(json_url)
    b = a.read()
    print a
    return b
