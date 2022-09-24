import pandas as pd
import csv

df =  pd.read_csv("total_stars.csv")

df.drop(['Unnamed:0','Unnamed:6','Star_name.1','Distance.1','Mass.1','Radius.1','Luminosity'],axis = 1,inplace=True)
finaldata = df.dropna()
print(finaldata)

