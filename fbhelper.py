#selenium
from selenium import webdriver
#keyboard manipulation
from selenium.webdriver.common.keys import Keys
#folder manipulation
import os
#env file for passwords and stuff
from dotenv import load_dotenv
#keep track of time
import time

#to read and edit excel files
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


#class to hold bot functions
class FbHelp:

    def __init__(self, username, password):
        #set class attributes
        self.username = username
        self.password = password

        #open webdriver chrome browser
        self.driver = webdriver.Chrome('./chromedriver.exe')


    #define logging in
    def login(self):
        #get instagram login page
        self.driver.get('https://www.facebook.com/login/device-based/regular/login/')
        #wait to load
        time.sleep(2)
        #find username box and password box by name attribute (from inspect element)
        #then send keys from self.username, self.password
        self.driver.find_element_by_name('email').send_keys(self.username)
        self.driver.find_element_by_name('pass').send_keys(self.password)
        #find and click login button as first element with text "Log In" in div (insepct element)
        self.driver.find_element_by_name('login').click()
        #time to load
        time.sleep(2)
        print('logged in')

    def closedriver(self):
        self.driver.close()
        print('closed out')

    def harvardfriends(self, friends_url):
        self.driver.get(friends_url)
        #wait to load
        time.sleep(2)
        
        '''
        if scroll too much elements will be unclickable :/
        '''
#        #initiate scroll pause time
#        SCROLL_PAUSE_TIME = 2
#
#        # Get scroll height
#        last_height = self.driver.execute_script("return document.body.scrollHeight")
#
#        while True:
#            # Scroll down to bottom
#            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#            # Wait to load page
#            time.sleep(SCROLL_PAUSE_TIME)
#
#            # Calculate new scroll height and compare with last scroll height
#            new_height = self.driver.execute_script("return document.body.scrollHeight")
#            if new_height == last_height:
#                break
#            last_height = new_height

        more_friends = True
        
        while more_friends:
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 200);")
            time.sleep(2)
            add_friend_buttons = self.driver.find_elements_by_xpath("//div[@aria-label='Add Friend']")
    
            for btn in add_friend_buttons:
                time.sleep(2)
                btn.click()
            
            # ask_more_friends = input('Scroll down for more add friend buttons?')
            ask_more_friends = 1

            if ask_more_friends == 0:
                more_friends = False

if __name__ == '__main__':
    #load env
    load_dotenv()
    #get password from env
    FB_PASSWORD = os.getenv('FB_PASSWORD')
    FB_USERNAME = os.getenv('FB_USERNAME')
    #class instance for setting username, password
    fbpy = FbHelp(FB_USERNAME,FB_PASSWORD)

    #actual actions
    
    #login
    fbpy.login()
    fbpy.harvardfriends('https://www.facebook.com/melissa.meng.714/friends_college')


    