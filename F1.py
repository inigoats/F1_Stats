import requests
from bs4 import BeautifulSoup
import lxml.html as lh
from bs4 import Comment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

#gets information from wikipedia, targets just the first table
table_f1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions', match="World Drivers' Champions by season")
len(table_f1)
print(f'Total tables: {len(table_f1)}')
df = table_f1[0]
df.columns = ["Season", "Driver", "Age", "Chassis", "Engine", "Tires", "Poles", "Wins", "Podiums", "Laps", "Points", "Points2", "CLinched", "RacesRemaining", "Margin", "Margin2"]
sp500_table= table_f1[0]

sp500_table = sp500_table.drop([73, 74])
sp500_table = sp500_table.drop(columns=['Engine', 'Tires', 'Poles', 'Podiums', 'Laps', 'Points2', "CLinched", "RacesRemaining", "Margin", "Margin2" ])
print(sp500_table)
df = sp500_table

df["Driver"]= df["Driver"].str[:-4]


df.head()
#df.info()

Season_Dict = df.set_index("Season").T.to_dict('index')
Driver_Dict = df.set_index("Driver").T.to_dict('series')
#comment out the table prints when finishing the script 

#table is done
#input how we want to find information. Name, Season(year)
Entered_Information = input(str("Would you like to find your information by the season, or driver? "))
Entered_Information = Entered_Information.lower()


if Entered_Information == "season":
    Season_Year = input("What year? ")
    Final_Season = df.loc[df.Season==Season_Year]
    print(Final_Season.to_string(index=False))
    
else:
    Driver_Name = input("Which driver? ")
    Final_Driver = df.loc[df.Driver==Driver_Name]
    print(Final_Driver.to_string(index=False))
    
#code to give back season year + info
#code to give back name + info


#Lewis_Hamilton = "Lewis Hamilton[51]"
#hammy = df["Driver"].values == Lewis_Hamilton
#print(df[hammy])
