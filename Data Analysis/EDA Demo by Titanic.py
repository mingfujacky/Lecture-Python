#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:15:59 2023

@author: jacky
"""
"""
data column: 
    乘客的艙等(pClass)
    性別(Sex)
    年齡(Age)
    兄弟姊妹＋老婆丈夫數量(SibSp)
    父母小孩的數量(Parch)
    票號(Ticket)
    票的費用(Fare)
    出發港口(Embarked)
    房間號碼(Cabin)
"""
import pandas as pd
import pandas.plotting._matplotlib
from ydata_profiling import ProfileReport

df = pd.read_csv("titanic.csv")
profile = ProfileReport(df, title="Auto EDA in Titanic Dataset")
profile.to_file("diabetes_Titanic.html")