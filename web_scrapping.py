#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 16:21:31 2025

@author: dkrasniqi
"""

#https://urlebird.com/fr/hash/mugler/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os 
from selenium.webdriver.chrome.service import Service
import requests

#%%
page = requests.get("https://www.etreproprio.com/annonces")
soup = BeautifulSoup(page.content, "html.parser")

#%%
#%%
temp = soup.find("div", class_='ep-search-list-wrapper').find_all("a")

#%%
liens = []
for i in range(len(temp)):
    print()
    if "https://www.etreproprio.com/immobilier-" in temp[i]['href']:
        liens.append(temp[i]['href'])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
