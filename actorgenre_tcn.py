# -*- coding: utf-8 -*-
"""ActorGenre_TCN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MBMRD2aSjymjy731jeR8ugauNCrEhSy8
"""

from __future__ import print_function

import pandas as pd

# Commented out IPython magic to ensure Python compatibility.
### above this cell is just setting data up for the model ###
### here is where we create and test the model ###
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import metrics
# %matplotlib inline

# export relevant_data as csv
import pandas as pd
name_genre_identifiers = pd.read_csv('name_genre_identifiers_final.csv', encoding='latin-1')
name_genre_identifiers = name_genre_identifiers[name_genre_identifiers['top genre'].notnull()][:100000]

names = name_genre_identifiers['primaryName']
top_genre = name_genre_identifiers['top genre']

X_train, X_test, y_train, y_test = train_test_split(names,top_genre,test_size = 0.2, random_state = 0)

from finetune.base_models import BERT, BERTLarge, GPT2, GPT2Medium, GPT2Large, TextCNN, TCN, RoBERTa, DistilBERT
from finetune import Classifier

model = Classifier(base_model = TCN)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred)

