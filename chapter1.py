#!/usr/bin/python
# -*- coding: utf-8 -*-

def q00():
    str = 'stressed'
    print(str[::-1])

def q01():
    str = 'パタトクカシーー'
    print(str[::2])

def q02():
    str1 = 'パトカー'
    str2 = 'タクシー'
    ans = ''
    for i, j in zip(str1, str2):
        ans += (i+j)
    print(ans)

def q03():
    str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    str = str.replace(',', '').replace('.', '')
    list = str.split(' ')
    ans = []
    for i, j in enumerate(list):
        ans.append(len(j))
    print(ans)

def q04():
    str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    str = str.replace('.', '')
    list = str.split(' ')
    ans = {}
    for i, j in enumerate(list):
        i += 1
        if i in (1, 5, 6, 7, 8, 9, 15, 16, 19):
            j = j[0]
        else:
            j = j[0] + j[1]
        ans[j] = i
    print(ans)

def q05():
    def ngram(s, n):
        ans = []
        for i in range(len(s)):
            if i < len(s)-n+1:
                ans.append(s[i:i+n])
        return ans

    str = 'I am an NLPer'
    print(ngram(str, 2))
    print(ngram(str.split(), 2))

def q06():
    def bigram(s):
        ans = []
        for i in range(len(s)):
            if i < len(s)-1:
                ans.append(s[i:i+2])
        return ans

    str1 = 'paraparaparadise'
    str2 = 'paragraph'
    X = bigram(str1)
    Y = bigram(str2)
    print(X)
    print(Y)
    setX = set(X)
    setY = set(Y)
    print(setX | setY)
    print(setX & setY)
    print(setX - setY)
    setse = set(['se'])
    if setX & setse:
        print('X include se')
    if setY & setse:
        print('Y include se')

def q07():
    def temprale(x, y, z):
        return '{0}時の{1}は{2}'.format(x, y, z)

    x = 12
    y = "気温"
    z = 22.4
    print(temprale(x, y, z))

def q08():
    def cipher(s):
        ans = ''
        for i in s:
            if i.islower():
                i = chr(219-ord(i))
            ans += i
        return ans

    str = 'I am an NLPer'
    print(cipher(str))
    print(cipher(cipher(str)))

def q09():
    import random
    str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    lis = str.split()
    ans = []
    for i in lis:
        if len(i) > 4:
            tmp = list(i[1:-1])
            random.shuffle(tmp)
            ans.append(i[0] + ''.join(tmp) + i[-1])
        else:
            ans.append(i)
    print(ans)

if __name__ == '__main__':
    q09()