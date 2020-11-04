import os
import pandas as pd
import numpy as np

# os.system("pwd")
# /Users/yungi/Documents/Hello_Atom/Titanic
for dirname, _, filenames in os.walk("/Users/yungi/Documents/Hello_Atom/Titanic/inputs"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = pd.read_csv("/Users/yungi/Documents/Hello_Atom/Titanic/inputs/train_and_test2.csv")
print(data.tail())