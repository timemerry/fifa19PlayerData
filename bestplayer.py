# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


data = pd.read_csv('data.csv')

print (data.loc[[11200,11201,11206,11226,11239],['Name','Age','Overall','Potential','Value']])
#print (data.loc[11206])