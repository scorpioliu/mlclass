#coding=utf8

'''
'''

from pylab import *
from scipy import *

def plotData(X, y):
    pos = find(y == 1)
    neg = find(y == 0)

    plot(X[pos, 0], X[pos, 1], 'b+')
    plot(X[neg, 0], X[neg, 1], 'ro')

    xlabel('Exam 1 score')
    ylabel('Exam 2 score')
    legend(['Admitted', 'Not admitted'])

def plotDecisionBoundary(theta, X, y):
    plotData(X[:, 1:3], y)
    if size(X, 1) <= 3:
        plot_x = hstack((min(X[:, 1]) - 2, max(X[:, 1]) + 2))
        plot_y = -(multiply(plot_x, theta[1]) + theta[0]) / theta[2]
        plot(plot_x.tolist()[0], plot_y.tolist()[0], 'k-')
        legend(('Admitted', 'Not admitted', 'Decision Boundary'))
        axis([30, 100, 30, 100])

sigmoid = lambda z: 1 / (1 + exp(-z))
#obfun = lambda a, x, y: -(y * log(array(sigmoid(x * a)))) + (1 - y) * log(1 - sigmoid(x * a)))).sum() / x.shape[0]

def predict(theta, X):
    return (sigmoid(qr_multiply(X * theta))).round()

def costFuction(theta, X, y):
    m = len(y)
    print(X.shape, theta.shape)
    hypo = sigmoid(X * theta)
    J = -sum(multiply(y, log(hypo)) + multiply((1 - y), log(1 - hypo))) / m 
    grad =  X.T * (hypo - y) / m
    return J, grad

def main():

    # part 1
    data = loadtxt('ex2data1.txt', delimiter = ',')
    X = data[:, [0, 1]]
    y = data[:, 2].T
    
    # part2
    m, n = X.shape
    X = hstack((ones((m, 1)), X))
    initial_theta = zeros((n + 1, 1))
    #print(obfun(initial_theta, X, y))
    print(costFuction(initial_theta, X, y))
   
    #theta = fmin(obfun, initial_theta, args = (X, y), maxiter = 10)
    
    # part3
    theta = [-24.9329, 0.204407, 0.199617]
    #plotDecisionBoundary(theta, X, y)
    #show()

    # part4
    prob = sigmoid(mat([1,45,85]) * mat(theta).T)
    print('for a student scores 45-85 probility is', prob)

    p = predict(mat(theta).T, X)
    print(mean(p==y) * 100)

if '__main__' == __name__:
    main()
