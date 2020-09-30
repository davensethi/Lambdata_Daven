"""This hopefully will get better"""

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

## df_explorer tries to let you explore your dataset faster

class TheStruggle:
  def __init__(self, input):
    """Takes in a DataFrame to explore easily """
    """Atribute"""

    self.X = input

  def df_explorer(self):
    print(self.X.head(10)),
    print(self.X.shape)
    print(self.X.info)

  ## df_cleaning helps you quickly git of 

    def df_no_zero_no_nan(self):
        self.X.replace(0, np.nan, inplace= True)
        self.X.dropna()
        return self.X.head(10)

class NotSureWorks:
  def __init__(self, target, df):
    ## X equals the data frame 
    ## y equals the targeted vector
    self.X = df.drop(columns = target, axis=1)
    self.y = df[target] 

  def NotSure(self):
    X_train, X_test, y_train, y_test = train_test_split(self.X,self.y, test_size=0.33)
    print(X_train)
    print(X_test)
    print(y_train)
    print(y_train)