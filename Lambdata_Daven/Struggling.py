"""This hopefully will get better"""

import pandas as pd 
import numpy as np

## df_explorer tries to let you explore your dataset faster


def df_explorer(df):
  print(df.head(10)),
  print(df.shape)
  print(df.info)

## df_cleaning helps you quickly git of 

  def df_no_zero_no_nan(df):
      df.replace(0, np.nan, inplace= True)
      df = df.dropna()
      return df.head(10)