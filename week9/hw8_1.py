#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:18:11 2020

@author: amanda
"""

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)



from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_esrimators=10)
clf.fit(train_x,train_y)
presiction =clf.presict(test_x)