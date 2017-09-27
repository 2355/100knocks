#!/usr/bin/python
# -*- coding: utf-8 -*-

import MeCab
import re
#import matplotlib.pyplot as plt

def c4():
    mecab = MeCab.Tagger()
    fr = open('neko.txt', 'r')
    fw = open('neko.txt.mecab', 'w')

    lines = fr.readlines()
    for line in lines:
        parse = mecab.parse(line)
        fw = open('neko.txt.mecab', 'a')
        fw.write(parse)

    fr.close()
    fw.close()

def q30():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    lis = []
    c = 0
    for line in lines:
        if not 'EOS' in line:
            dic = {}
            l = re.split(r',|\t', line)
            dic['surface'] = l[0]
            dic['base'] = l[7]
            dic['pos'] = l[1]
            dic['pos1'] = l[2]
            lis.append(dic)
        else:
            if lis:
                print(lis)
            lis = []
            c += 1
        if c > 10:
            break

    fr.close()

def q31():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    lis = []
    c = 0
    for line in lines:
        if not 'EOS' in line:
            dic = {}
            l = re.split(r',|\t', line)
            dic['surface'] = l[0]
            dic['base'] = l[7]
            dic['pos'] = l[1]
            dic['pos1'] = l[2]
            lis.append(dic)
            if dic['pos'] == '動詞':
                print(dic['surface'])
        else:
            lis = []
            c += 1
        if c > 10:
            break

    fr.close()

def q32():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    lis = []
    c = 0
    for line in lines:
        if not 'EOS' in line:
            dic = {}
            l = re.split(r',|\t', line)
            dic['surface'] = l[0]
            dic['base'] = l[7]
            dic['pos'] = l[1]
            dic['pos1'] = l[2]
            lis.append(dic)
            if dic['pos'] == '動詞':
                print(dic['base'])
        else:
            lis = []
            c += 1
        if c > 10:
            break

    fr.close()

def q33():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    lis = []
    c = 0
    for line in lines:
        if not 'EOS' in line:
            dic = {}
            l = re.split(r',|\t', line)
            dic['surface'] = l[0]
            dic['base'] = l[7]
            dic['pos'] = l[1]
            dic['pos1'] = l[2]
            lis.append(dic)
            if dic['pos'] == '名詞' and dic['pos1'] == 'サ変接続':
                print(dic['base'])
        else:
            lis = []
            c += 1
        if c > 100:
            break

    fr.close()

def q34():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    lis = []
    c = 0
    for line in lines:
        if not 'EOS' in line:
            dic = {}
            l = re.split(r',|\t', line)
            dic['surface'] = l[0]
            dic['base'] = l[7]
            dic['pos'] = l[1]
            dic['pos1'] = l[2]
            lis.append(dic)
        else:
            for i in range(len(lis)-2):
                if lis[i]['pos'] == '名詞' \
                    and lis[i+1]['surface'] == 'の' \
                    and lis[i+2]['pos'] == '名詞':
                    print(lis[i]['surface'], lis[i+1]['surface'], lis[i+2]['surface'])
            lis = []
            c += 1
        if c > 100:
            break

    fr.close()

def q35():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    lis = []
    c = 0
    for line in lines:
        rensetsu = []
        if not 'EOS' in line:
            dic = {}
            l = re.split(r',|\t', line)
            dic['surface'] = l[0]
            dic['base'] = l[7]
            dic['pos'] = l[1]
            dic['pos1'] = l[2]
            lis.append(dic)
        else:
            for i in lis:
                if i['pos'] == '名詞':
                    rensetsu.append(i['surface'])
                else:
                    if len(rensetsu) > 1:
                        print(''.join(rensetsu))
                    rensetsu = []
            lis = []
            c += 1
        if c > 100:
            break

    fr.close()

def q36():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    dic = {}
    for line in lines:
        if not 'EOS' in line:
            l = re.split(r',|\t', line)
            dic[l[0]] = 0

    for line in lines:
        if not 'EOS' in line:
            l = re.split(r',|\t', line)
            dic[l[0]] += 1

    for k, v in sorted(dic.items(), key=lambda x:x[1], reverse=True):
        print(k, v)

    fr.close()

# unfinished
def q37():
    fr = open('neko.txt.mecab', 'r', encoding='UTF-8')
    lines = fr.readlines()
    dic = {}
    for line in lines:
        if not 'EOS' in line:
            l = re.split(r',|\t', line)
            dic[l[0]] = 0

    for line in lines:
        if not 'EOS' in line:
            l = re.split(r',|\t', line)
            dic[l[0]] += 1

    k_list = []
    v_list=[]
    n = 0
    for k, v in sorted(dic.items(), key=lambda x:x[1], reverse=True):
        n += 1
        if n > 10:
            break
        k_list.append(k)
        v_list.append(v)

    print(k_list)
    print(v_list)

    fr.close()


if __name__ == '__main__':
    q37()