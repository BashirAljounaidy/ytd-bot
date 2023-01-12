#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 04:18:13 2023

@author: bashir
"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


class Uploader :
    def __init__ (self,profile_path):
        self.profile_path = '/Users/bashir/Library/Application Support/Google/Chrome/myprofile'
        self.options = uc.ChromeOptions()
        #setting profile
        self.options.user_data_dir = self.profile_path
        self.driver = self.uc.Chrome(options=self.options)
        self.url='https://studio.youtube.com/channel/UCH4fTtYeGAfwgV3Gct0Nt9g/videos?d=ud'
        
        self.upload_loc=self.driver.find_element(By.XPATH,"//input[@type='file']")
        self.locator1.send_keys("/Users/bashir/Documents/projects/ytd-bot/مقلب حليب الحمار بالخال بوطلال.mp4")

