#coding = utf8

'''
simple k-means code
it's very sensitive on initial point selection
because I don't handle the situation that some class set is empty

by scorpioLiu
created on 2012.9.7
'''

from numpy import *
from pylab import *

def plotData(data, arg):
    x = data[:, 0]
    y = data[:, 1]
    plt.plot(x, y, arg)
    axis([0, 10, 0, 10])

def calDist(data, centers):
    return  array([sum((data - c) ** 2, axis = 1) for c in centers]).T

# Initialization
nCenter = 3
data = vstack(randint(0, 10, (5, 2))/8.0 + [2,2])
data = vstack((randint(0, 10, (5, 2))/8.0 + [5,5], data))
data = vstack((randint(0, 10, (5, 2))/8.0 + [3,6], data))
centers = resize([1,1,7,4,3,9], (3,2))

plotData(data, 'ko')
plotData(centers, 'bo')

# Iteration
cnt = 0
while True:
    oldcenters = array(centers)
    d = calDist(data, centers)
    z = array([min(d[i, :]) for i in range(size(data, 0))]).T
    idx = array([j for i in range(size(data, 0)) for j in range(nCenter) if d[i, j] == z[i]])    
    
    centers = vstack([mean(data[find(idx == c),:], 0) for c in range(nCenter)])
    cnt += 1
    if sum(centers - oldcenters) == 0: break

plotData(centers, 'ro')
title('%d circles'% cnt)
legend(('data', 'initial center', 'final center'))
show() 
