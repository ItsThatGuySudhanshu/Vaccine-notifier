# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:15:37 2021

@author: sudha
"""

import requests, bs4
import datetime, time

while True :
    
   
    if datetime.datetime.now().minute % 5 == 0: 
        covidUNCWebsite = requests.get("https://www.unchealthcare.org/coronavirus/vaccines/phase-1b-covid-19-vaccine/")
        
        doingSoup = bs4.BeautifulSoup(covidUNCWebsite.text, 'html.parser')
        
        divs = doingSoup.select(".cmsPageContent > h3")
        
        
        
        text = divs[0].text
        
        print(text)
        
        textNoAppointments = "We’re very sorry, but all vaccine appointments have been scheduled."
        
        if text != textNoAppointments:
            print("found appointment")
            requests.post("https://maker.ifttt.com/trigger/covidNotifications/with/key/kyIjnyQthEWkDcRnUpU-ohy-DL_9WmxTq2ItMsgDQoz")
                     
    print("sleeping")            
            
    time.sleep(60)
   

