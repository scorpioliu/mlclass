#coding = utf8
#!/usr/bin/python

'''
use kmeans to cluster weibo

by scorpioLiu
created on 2012.9.7
'''
 
from numpy import *
from pylab import *
import networkx as nx
import Pycluster

def checkFeature(w):
    if len(w) == 1: return False
    flag = False
    for c in w:
        if ord(c) <= 0x9fa5 and ord(c) >= 0x4e00:
            flag = True
            break
    return flag

# get all feature 
feature = {}
raw = []
for line in open('../data/weibo_cluster_sample.txt'):
    line = line.decode('utf8').split()
    raw.append(line)
    for w in line:
        if checkFeature(w): feature[w] = 0
print('feature size is', len(feature))
feature = list(feature)

# give each case feature vector
weibo = []
for case in raw:
    case = set(case)
    f = []
    for i in feature:
        if i in case:
            f.append(1.0)
        else:
            f.append(0.0)
    weibo.append(f)
weibo = array(weibo)

# kmeans for 2 clusters
labels, error, nfound = Pycluster.kcluster(weibo, 2)
word = {}
for sen in array(raw)[find(labels == 0), :]:
    for w in sen:
        if w not in word: word[w] = 0
        word[w] += 1
tag = sorted([[w, f] for (w, f) in word.items() if f > 3 and w in feature], key = lambda x:x[1], reverse = True)

testLabel = ones((1, 100))[0]
testLabel[51:100] = 0
precious =(sum(testLabel == labels) / 100.0)
print(labels)
print('precious is', max(precious, 1-precious))

# draw tag network
tagSet = {}
cnt = 0
for i in tag:
    tagSet[i[0]] = cnt
    cnt += 1
print(len(tag), len(tagSet))
G = nx.Graph()
cnt = 0
for i in tag:
    G.add_node(cnt)
    cnt += 1
for sen in array(raw)[find(labels == 0), :]:
    for i in range(len(sen) - 1):
        for j in range(i, len(sen)):
            if sen[i] in tagSet and sen[j] in tagSet:
                G.add_edge(tagSet[sen[i]], tagSet[sen[j]])
         
cnt = 0
fo = open('res.txt','w')
for i in tag:
    fo.write('%d %s\n' % (cnt, i[0].encode('utf8')))
    cnt += 1
fo.close()
nx.draw(G, node_size=[i[1]*70 for i in tag], node_color=[float(G.degree(v)) for v in G])
show()

