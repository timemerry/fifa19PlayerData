# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')

print (data.loc[11200:11250,['Name','Age','Value','Position','Overall','Potential']])

