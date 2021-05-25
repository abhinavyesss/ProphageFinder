#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import time

import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    load_dotenv()
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    bot = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'), options = options)
    bot.get('http://dmk-brain.ecn.uiowa.edu/pVOGs/VOGbigtable.html#')
    time.sleep(5)

    inp = bot.find_element_by_xpath('.//select[@name = "POGs_table_length"]')
    inp.click()
    time.sleep(0.5)
    inp = bot.find_element_by_xpath('.//option[@value = "-1"]')
    inp.click()
    time.sleep(0.5)

    l = []
    inp = bot.find_elements_by_class_name('odd')
    for i in inp:
        print(i)
        l.append(i.get_attribute('innerHTML'))

    inp = bot.find_elements_by_class_name('even')
    for i in inp:
        print(i)
        l.append(i.get_attribute('innerHTML'))

    pickle.dump(l, open('{}voglist.txt'.format(os.getenv('BASE_PATH')), 'wb'))

    time.sleep(4)
    bot.close()
    bot.quit()
