#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:50:50 2020

@author: amanda
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 05:21:20 2020

@author: amanda
"""

import pandas as pd

from sklearn.utils import shuffle

from sklearn import tree
from sklearn.metrics import accuracy_score
df = pd.read_csv('./HW7_2.csv')
#print(df.dtypes)
#print(df.shape)
train_size = df.shape[0] * 10/11
test_size = df.shape[0] * 1/11
#print(train_size)
#print(test_size)
df[df['fraud_ind'] == 1][1000:1200]
# Y = df['fraud_ind']
# X = df.drop(['fraud_ind'], axis=1)

ecfg = pd.get_dummies(df.ecfg)
flbmk = pd.get_dummies(df.flbmk)

flg_3dsmk = pd.get_dummies(df.flg_3dsmk)
insfg = pd.get_dummies(df.insfg)
ovrlt = pd.get_dummies(df.ovrlt)
#print('='*10)
#print(ovrlt)
#display(df.ovrlt)
#print('='*10)
df = df.drop(['flbmk'], axis = 1)
dummy_ecfg = ecfg["Y"].tolist()
dummy_flg_3dsmk = flg_3dsmk["Y"].tolist()
dummy_insfg = insfg["Y"].tolist()
dummy_ovrlt = ovrlt["Y"].tolist()

df['ecfg'] = dummy_ecfg
df['flg_3dsmk'] = dummy_flg_3dsmk
df['insfg'] = dummy_insfg
df['ovrlt'] = dummy_ovrlt

# input_data = X.values.tolist()
test_x = df[1000:1200]
test_y = test_x['fraud_ind']
test_x = test_x.drop(['fraud_ind'], axis=1)

train_x = df.drop(df.index[1000:1200])
train_y = train_x['fraud_ind']
train_x = train_x.drop(['fraud_ind'], axis=1)
#print(test_x.shape)
#print(train_x.shape)
shuf_train_x, shuf_train_y = shuffle(train_x, train_y)
shuf_test_x, shuf_test_y = shuffle(test_x, test_y)
clf = tree.DecisionTreeClassifier()
clf.fit(shuf_train_x, shuf_train_y)

pred = clf.predict(shuf_test_x)
acc = accuracy_score(shuf_test_y, pred)
#print(acc)
from sklearn import svm
a = svm.SVC()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)

from sklearn.metrics import accuracy_score
a = accuracy_score(test_y, prediction)
print("svm: ",a)
#svm

from sklearn import tree

b = tree.DecisionTreeClassifier()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)

from sklearn.metrics import accuracy_score
b = accuracy_score(test_y, prediction)
print("tree: ",b)
#tree

from sklearn.neural_network import MLPClassifier
c = MLPClassifier(hidden_layer_sizes=(20,))
clf.fit(train_x,train_y)    

prediction = clf.predict(test_x)

from sklearn.metrics import accuracy_score
c = accuracy_score(test_y, prediction)
print("mlp: ",c)
#mlp

from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

iris = datasets.load_iris()
X, y = iris.data[:, 1:3], iris.target

a = svm.SVC(probability=True, random_state = 0)
b = tree.DecisionTreeClassifier(random_state = 0) 
c = MLPClassifier(hidden_layer_sizes = (20, ), random_state = 0)

vt = VotingClassifier(
    estimators=[('svc', a), ('tree', b), ('mlp', c)],
    voting='soft')

d = accuracy_score(test_y, prediction)
print("最終: ",d)


