# -*- coding: utf-8 -*-
"""

Created on Sat Jun 20 00:10:58 2020

@author: Srujan Deshpande
"""
import time
import random
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd




option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu");

prefs = {'download.default_directory' : 'C:\\Users\\Srujan Deshpande\\Downloads\\cult\\kriti'}
option.add_experimental_option('prefs', prefs)


browser = webdriver.Chrome(executable_path=r'C:\Users\Srujan Deshpande\chromedriver.exe', chrome_options=option)



    
link = "https://d3pyi18cmxgkxc.cloudfront.net/out/v1/f53f110f44ed4c90a29450d02d83dc70/index_1_"
#link = "https://d2ga8i2dkfrq74.cloudfront.net/out/v1/e9412e0c75864d4bbe967fa605798034/index_1_"
ext = ".ts"

for i in range(535,801):
    browser.get(link+str(i)+ext)    

import shutil
with open('C:\\Users\\Srujan Deshpande\\Downloads\\cult\\jacq_dance_1\\merged.ts', 'wb') as merged:
    for i in range(250,451):
        ts_file = 'C:\\Users\\Srujan Deshpande\\Downloads\\cult\\jacq_dance_1\\index_3_'+str(i)+'.ts'
        #for ts_file in ts_filenames:
        with open(ts_file, 'rb') as mergefile:
            shutil.copyfileobj(mergefile, merged)
    for i in range(451,505):
        ts_file = 'C:\\Users\\Srujan Deshpande\\Downloads\\cult\\jacq_dance_1\\index_1_'+str(i)+'.ts'
        #for ts_file in ts_filenames:
        with open(ts_file, 'rb') as mergefile:
            shutil.copyfileobj(mergefile, merged)
            
            
import subprocess

infile = 'C:\\Users\\Srujan Deshpande\\Downloads\\culttest01\\merged.ts'
outfile = 'C:\\Users\\Srujan Deshpande\\Downloads\\culttest01\\merged.mp4'

subprocess.run(['ffmpeg', '-i', infile, outfile])