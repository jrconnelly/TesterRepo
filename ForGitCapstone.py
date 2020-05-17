#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[1]:


print (" Hello Capstone Project Course")
import pandas as pd
import numpy as np
import requests # library to handle requests
import urllib.request # scraper from tutorial 
# warning easyinstall will be removed in future version
get_ipython().system('easy_install beautifulsoup4')
get_ipython().system('pip install lxml # one parser')
#!apt-get install python-lxml #another parser
get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
from bs4 import BeautifulSoup
### forum for foursquare
#%capture
#!pip install geocoder


# In[2]:


# COMMENT UNCOMMENT for READTHIS PART WORKS------------------------------------##
df_latlon = pd.read_csv('http://cocl.us/Geospatial_data')
df_latlon.head()
df_latlon.rename(columns={'Postal Code':'PostalCode'},inplace=True)
df_latlon['PostalCode']
# This works end -----------------
#This  request for data provided works begin =================
url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
#from bs4 import BeautifulSoup
req = requests.get(url)
table = req.content
df = pd.read_html(str(table))
neighborhood=pd.DataFrame(df[0])
## this works end ===============
# Clean up column names, remove \n
# This works -------begin
#df.rename(columns={'Postal Code':'PostalCode'},inplace=True)
#add regular expressions to import resources
import pandas as pd
import re
# line below works before processing below but not after
#neighborhood=pd.DataFrame(df[0])
#neighborhood.rename(columns={'Postal Code\\n':'PostalCode'},inplace=True)
neighborhood.rename(columns={'Borough\\n':'Borough'},inplace=True)
neighborhood.rename(columns={'Postal Code\\n':'PostalCode'},inplace=True)
neighborhood.rename(columns={'Neighborhood\\n':'Neighborhood'},inplace=True)
#neighborhood.Borough
#neighborhood.PostalCode
neighborhood
#df_latlon.shape
#neighborhood.shape
pd.merge(df_latlon, neighborhood, on='PostalCode')


# In[ ]:




