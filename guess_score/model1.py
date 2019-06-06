# coding:utf-8
import numpy as np
from sklearn import tree

p = [100,97,94,91]
score = [97.6, 97.6, 97.3, 99.4, 96.1, 97.6, 99.4, 96.7, 97.6, 96.1, 98.2, 96.55]
# [hong,xiong,zhuang,wang,zhang]
alpha = [[0.4, 0.1, 0.1, 0.3, 0.1],# MM
   [0.4, 0.1, 0.3, 0.1, 0.1],# RCS
   [0.4, 0.1, 0.1, 0.3, 0.1],# Cloud
   [0.4, 0.1, 0.3, 0.1, 0.1],# Platform
   [0.4, 0.1, 0.1, 0.3, 0.1],# Market
   [0.4, 0.3, 0.1, 0.1, 0.1],# RD
   [0.4, 0.1, 0.3, 0.1, 0.1],# System
   [0.4, 0.3, 0.1, 0.1, 0.1],# Quality
   [0.4, 0.1, 0.1, 0.3, 0.1],# General
   [0.4, 0.3, 0.1, 0.1, 0.1],# Finance
   [0.4, 0.15, 0.15, 0.15, 0.15],# HR
   [0.4, 0.15, 0.15, 0.15, 0.15]# Party
]

get_raw_scores = lambda p,score,alpha: [[i+1,score[i],[x for x in [[x1,x2,x3,x4,x5] 
	for x1 in p for x2 in p for x3 in p for x4 in p for x5 in p] 
	if score[i] == np.dot(alpha[i],x)]] 
	for i in range(len(score))]

def make_X(X, x, raw_scores, i):
	x_i = raw_scores[i][2]
	if i == len(raw_scores) - 1:
		for x_i_j in x_i:
			new_x = x + [x_i_j]
			X.append(new_x)
	else:
		for x_i_j in x_i:
			new_x = x + [x_i_j]
			make_X(X, new_x, raw_scores, i+1)

def get_y1(raw_scores,X_set):
	y1_set = []
	for X in X_set:
		X1 = np.array(X)
		XT = X1.T
		x_j = []
		y1 = 0
		for XT_j in XT:
			x_j.append(np.average(XT_j))
		for j in range(5):
			y1_j = 0
			for i in range(12):
				y1_j += np.power((X[i][j] - x_j[j]),2) / 12
			y1 += y1_j
	y1_set.append(y1)
	return y1_set

def get_y2(raw_scores,X_set):
	y2_set = []
	for X in X_set:
		y2 = 0
		for i in range(12):
			y2_i = 0
			x_i = np.average(X[i])
			for j in range(5):
				y2_i += np.power((X[i][j] - x_i,2) / 5
			y2 += y2_i
	y2_set.append(y2)
	return y2_set

raw_scores = get_raw_scores(p, score, alpha)
# X_set = []
# make_X(X_set, [], raw_scores, 0)
