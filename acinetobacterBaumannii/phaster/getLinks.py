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
    bot.get('https://www.ncbi.nlm.nih.gov/genome/browse/#!/prokaryotes/403/')

    time.sleep(10)

    links = []

    for pages in range(2, 106):
        for a in bot.find_elements_by_xpath('.//a'):
            href = a.get_attribute('href')
            try:
                if 'nlm.nih.gov/nuccore/' in href and href != 'https://www.ncbi.nlm.nih.gov/nuccore/':
                    links.append(href)
            except:
                pass
        try:
            pgINP = bot.find_element_by_class_name('ui-pg-input')
            pgINP.clear()
            pgINP.send_keys(pages)
            pgINP.send_keys(Keys.RETURN)
            time.sleep(4.5)
        except:
            pass
        finally:
            print('{} links present.'.format(len(links)))
            time.sleep(2)
    
    f = open('{}phaster/linklist.txt'.format(os.getenv('MAIN_PATH')), 'wb')
    pickle.dump(links, f)
    f.close()

    print('{} links were extracted.'.format(len(links)))

    time.sleep(4)
    bot.close()
    bot.quit()
    