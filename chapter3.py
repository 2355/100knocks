#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re
import urllib.request
import urllib.parse

def q20():
    f = open('jawiki-country.json', 'r')
    lines = f.readlines()
    for line in lines:
        wiki = json.loads(line)
        if wiki['title'] == 'イギリス':
            uk = wiki['text']
    return uk

def q21(uk):
    for line in uk.splitlines():
        if re.search('category', line, re.I):
            print(line)

def q22(uk):
    for line in uk.splitlines():
        if re.search('category', line, re.I):
            print(line.replace('[[Category:', '').replace(']]', ''))

def q23(uk):
    for line in uk.splitlines():
        if re.search('==', line):
            n = int(line.count('=')/2-1)
            print(line.replace('=', ''), 'level', n)

def q24(uk):
    for line in uk.splitlines():
        if re.search('(ファイル|File)', line, re.I):
            line = re.sub('^\|', '', line)
            line = re.sub('\|.*$', '', line)
            line = re.sub('^.*?\[\[', '', line)
            line = re.sub('^(ファイル|File):', '', line)
            print(line)

def q25(uk):
    dic = {}
    for line in uk.splitlines():
        if re.search('^}}$', line):
            break
        if re.search('^\|', line):
            key = re.sub('^\|', '', line)
            key = re.sub(' =.*', '', key)
            val = re.sub('^.*?= ', '', line)
            dic[key] = val

    print(dic)
    for k, v in dic.items():
        print(k, ':', v)

def q26(uk):
    dic = {}
    for line in uk.splitlines():
        if re.search('^}}$', line):
            break
        if re.search('^\|', line):
            key = re.sub('^\|', '', line)
            key = re.sub(' =.*', '', key)
            val = re.sub('^.*?= ', '', line)
            if re.search("''(.*?)''", val):
                val = re.sub("'{2,5}", '', val)
            dic[key] = val

    print(dic)
    for k, v in dic.items():
        print(k, ':', v)

def q27(uk):
    dic = {}
    for line in uk.splitlines():
        if re.search('^}}$', line):
            break
        if re.search('^\|', line):
            key = re.sub('^\|', '', line)
            key = re.sub(' =.*', '', key)
            val = re.sub('^.*?= ', '', line)
            if re.search("''(.*?)''", val):
                val = re.sub("'{2,5}", '', val)
            if re.search("\[\[(.*?)\]\]", val):
                val = re.sub("\[\[", '', val)
                val = re.sub("\]\]", '', val)
            dic[key] = val

    print(dic)
    for k, v in dic.items():
        print(k, ':', v)

def q28(uk):
    dic = {}
    for line in uk.splitlines():
        if re.search('^}}$', line):
            break
        if re.search('^\|', line):
            key = re.sub('^\|', '', line)
            key = re.sub(' =.*', '', key)
            val = re.sub('^.*?= ', '', line)
            if re.search("''(.*?)''", val):
                val = re.sub("'{2,5}", '', val)
            if re.search("\[\[(.*?)\]\]", val):
                val = re.sub("\[\[", '', val)
                val = re.sub("\]\]", '', val)
            val = re.sub("<(.*?)>", '', val)
            val = re.sub("\[http://(.*?)\]", '', val)
            dic[key] = val

    print(dic)
    for k, v in dic.items():
        print(k, ':', v)

def q29(uk):
    for line in uk.splitlines():

        if re.search('国旗画像', line):
            file_name = re.sub("^(.*?) = ", '', line)
    file_name = urllib.parse.quote_plus(file_name)
    term = 'https://www.mediawiki.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&titles=File:'
    term = term + file_name
    post = urllib.request.urlopen(term)
    pos = post.read().decode('utf-8')
    j = json.loads(pos)
    print(j['query']['pages']['-1']['imageinfo'][0]['url'])


if __name__ == '__main__':
    uk = q20()
    #print(uk)
    q29(uk)