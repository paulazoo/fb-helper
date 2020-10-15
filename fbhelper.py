#selenium
from selenium import webdriver
#keyboard manipulation
from selenium.webdriver.common.keys import Keys
#webdriver options
from selenium.webdriver.chrome.options import Options
#folder manipulation
import os
#env file for passwords and stuff
from dotenv import load_dotenv
#keep track of time
import time
#datetime
from datetime import datetime
from datetime import date
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

        #set up chrome driver
        option = Options()

        #stop notif popup
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2 
        })

        #open webdriver chrome browser
        self.driver = webdriver.Chrome(chrome_options=option, executable_path='./chromedriver.exe')

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

    def harvardfriends(self, friends_url, max_friend_requests):
        friend_requests_sent = 0
        skip = 0

        self.driver.get(friends_url)
        #wait to load
        time.sleep(10)
        
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
                try:
                    btn.click()
                    friend_requests_sent = friend_requests_sent + 1
                except:
                    try:
                        self.driver.find_element_by_xpath("//div[@aria-label='Close']").click()
                        skip = skip + 1
                    except:
                        print("An exception occurred")
            
            if friend_requests_sent != 0:
                print(friend_requests_sent)

            # ask_more_friends = input('Scroll down for more add friend buttons?')
            ask_more_friends = 1

            if ask_more_friends == 0 or friend_requests_sent > max_friend_requests:
                more_friends = False

    def chill(self, max_chilling_time):
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        chilling_time = 0
        
        while chilling_time < max_chilling_time:
            chilling_time = chilling_time + 1
            self.driver.get('https://congregate.live')
            time.sleep(20)
            self.driver.get('https://class.congregate.live')
            time.sleep(20)
            self.driver.get('https://collegearch.org')
            time.sleep(20)
            print('chilling...')
            print(chilling_time)

        print('chill finished!')
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(chilling_time)


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
    
    # fbpy.harvardfriends('https://www.facebook.com/melissa.meng.714/friends_college')
    
    today = str(date.today())
    if today == '2020-10-15':
        fbpy.harvardfriends('https://www.facebook.com/groups/516889128701490/members/things_in_common', 500)
    elif today == '2020-10-16':
        fbpy.harvardfriends('https://www.facebook.com/groups/455303088290544/members/things_in_common', 500)
    elif today == '2020-10-17':
        fbpy.harvardfriends('https://www.facebook.com/groups/455303088290544/members/things_in_common', 500)
    else:
        fbpy.harvardfriends('https://www.facebook.com/groups/zoommemes/members/things_in_common', 500)
        