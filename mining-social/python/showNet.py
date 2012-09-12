#coding=utf8

'''
show the touchpal followers in twitter

by scorpioLiu
created on 2012.9.7
'''
import networkx as nx
from pylab import *
from networkx import graphviz_layout

nodeFile = '../data/twitter_node.txt'
mainNode = 'TouchPal'

G = nx.Graph()
G.add_node(mainNode)

cnt = 0
subcnt = 0
node = {}
flag = False
m = ''
famous = {}
for line in open(nodeFile):
    if '=' in line:
        cnt += 1
        m = line[:-1].replace('===', '')
        if cnt % 30 == 0:
            flag = True
            subcnt = 0
            G.add_node(m)
            G.add_edge(mainNode, m)
        else:
            flag = False
        continue
    elif flag:
        subcnt += 1
        n = line[:-1]
        if subcnt % 30 == 0:
            G.add_node(n)
            G.add_edge(m,n)
        if subcnt > 3000:
            famous[m] = 0

figure(figsize=(8,8))
nx.draw(G, node_color = [[float(G.degree(v)) for v in G]], 
alpha = 0.5, node_size = [G.degree(v) for v in G], with_labels = False)
print(famous)

show()
