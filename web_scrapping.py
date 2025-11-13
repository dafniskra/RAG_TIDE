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

for j in range(1):
    page = requests.get("https://www.etreproprio.com/annonces/thflcpo.odd.g"+str(j)+"#list")
    soup = BeautifulSoup(page.content, "html.parser")

    temp = soup.find("div", class_='ep-search-list-wrapper').find_all("a")
    
    liens = []
    for i in range(len(temp)):

        if "https://www.etreproprio.com/immobilier-" in temp[i]['href']:
            liens.append(temp[i]['href'])

    for lien in liens:
        
        
        options = webdriver.ChromeOptions()
         
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=options)
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.set_window_size(1000, 800)
        driver.get(lien)
        time.sleep(5)
            
        #%%
        page_source = driver.page_source
        soup_ = BeautifulSoup(page_source, 'lxml')
        
        driver.close()
        
        try:
            prix = soup_.find("div", class_='ep-price').text.replace(" ", "")
        except:
            prix=0
        
        try:
            ch = soup_.find("div", class_='ep-ff-room-area').find("div", class_='ep-room').text.replace(" ", "")
        except:
            ch=0
        
        
        print("page: ", j, ", prix: ", prix,', chambre: ',ch)
    






  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
