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
sp500_table= table_f1[0]
print(sp500_table)

df.head()
#df.info()

#comment out the table prints when finishing the script 

#table is done
#input how we want to find information. Name, Season(year)
Entered_Information = input(str("Would you like to find your information by the season, or driver? "))
Entered_Information = Entered_Information.lower()

if Entered_Information == "season":
    Season_Year = print(input("What year? "))
else:
    Driver_Name = print(input(str("Which driver? ")))
    Driver_Name = Driver_Name.lower()
#code to give back season year + info
#code to give back name + info


#Lewis_Hamilton = "Lewis Hamilton[51]"
#hammy = df["Driver"].values == Lewis_Hamilton
#print(df[hammy])
