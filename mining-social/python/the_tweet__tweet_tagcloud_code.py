# -*- coding: utf-8 -*-

'''
example code to create a tag cloud

by scorpioLiu
created on 2012.9.7
'''

import os
import sys
import webbrowser
import json
from math import log

def checkWord(w):
    if len(w) < 2 or '/' in w or w == 'of': return False
    flag = False
    for c in w:
        if c in stopchar: return False
        if c.isalpha(): flag = True
    return flag

def weightFreq(f):
    if wmin == wmax: return MAX_FONT_SIZE
    return (f - wmin) * (MAX_FONT_SIZE - MIN_FONT_SIZE) / (wmax - wmin) + MIN_FONT_SIZE

HTML_TEMPLATE = '../web/tagcloud_template.html'
rawfile = '../data/weibo_me.txt'
MAX_FONT_SIZE = 13
MIN_FONT_SIZE = 3

stopchar = {w.decode('utf8')[:-1] for w in open('../data/stop_char.txt')}

word = {}
for line in open(rawfile):
    line = line.decode('utf8').split()
    for w in line:
        if not checkWord(w): continue
        if w not in word: word[w] = 0
        word[w] += 1

raw = sorted([[w, '', f] for (w, f) in word.items() if f > 1], key = lambda x:x[2], reverse = True)

wmin = raw[-1][2]
wmax = raw[0][2]

weighted_output = [[i[0], i[1], weightFreq(i[2])] for i in raw]

# Substitute the JSON data structure into the template

html_page = open(HTML_TEMPLATE).read() % \
                 (json.dumps(weighted_output),)

if not os.path.isdir('out'):
    os.mkdir('out')

f = open(os.path.join('out', os.path.basename(HTML_TEMPLATE)), 'w')
f.write(html_page)
f.close()

print 'Tagcloud stored in: %s' % f.name

# Open up the web page in your browser
webbrowser.open("file://" + os.path.join(os.getcwd(), 'out', os.path.basename(HTML_TEMPLATE)))
