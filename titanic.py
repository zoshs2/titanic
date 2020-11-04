'''
Overview

This is the original data from Titanic competition plus some changes that I applied to it to be better suited for binary logistic regression:

1. Merged the train and test data.
2. Removed the 'ticket' and 'cabin' attributes.
3. Moved the 'Survived' attribute to the last column.
4. Added extra zero columns for categorical inputs to be better suited for One-Hot-Encoding.
5. Substituted the values of 'Sex' and 'Embarked' attributes with binary and categorical values respectively.
6. Filled the missing values in 'Age' and 'Fare' attributes with the median of the data.
'''

import os # Operating System Control
import pandas as pd # Data Processing
import numpy as np # Linear Algebra

# os.system("pwd")
# /Users/yungi/Documents/Hello_Atom/Titanic
for dirname, _, filenames in os.walk("/Users/yungi/Documents/Hello_Atom/Titanic/inputs"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = pd.read_csv("/Users/yungi/Documents/Hello_Atom/Titanic/inputs/train_and_test2.csv")

## Importing Libraries
import matplotlib.pyplot as plt
import seaborn as sns

## Modeling Libraries
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier # Study
from sklearn.ensemble import RandomForestClassifier # Study
## Evaluate Model
from sklearn.metrics import confusion_matrix, roc_curve

## Data Preprocessing
print(data.head())




