#!/usr/bin/python
# -*- encoding:utf-8 -*-

from bs4 import BeautifulSoup
import  requests
import sqlite3

def get_item_info(url):
#url='http://jobs.zhaopin.com/120533378250136.htm?ssidkey=y&ss=201&ff=03&sg=4105be3091124f30a920b81dd007602b&so=1'

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title_list = soup.select('div.fl > h1')
    title = title_list[0].text
    company_list = soup.select('div.fl > h2')
    company = company_list[0].text
    monthlypay_list = soup.select('div.terminalpage-left > ul > li > strong')
    monthlypay = monthlypay_list[0].text
    experience_list = soup.select('div.terminalpage-left > ul > li')
    experience = experience_list[4].text
    Education_list = soup.select('div.terminalpage-left > ul > li')
    Education = Education_list[5].text

    data = {
        'title' : title,
        'company' : company,
        'monthlypay' : monthlypay,
        'experience' : experience,
        'Education' : Education
    }

    print(data)

def get_all_item_info():
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9F%B3%E5%B7%9E&kw=java&sm=0&p=1&isfilter=0&fl=786&isadv=0'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    hrefs_list = soup.select('td.zwmc > div > a')
    for href in hrefs_list:
        link = href.get('href')
        if 'jobs' in link:

            get_item_info(link)
get_all_item_info()





