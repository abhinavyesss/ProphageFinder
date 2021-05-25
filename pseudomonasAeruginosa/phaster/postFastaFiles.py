#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import time
import requests

import pickle
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    
    load_dotenv()

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    bot = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'), options = options)

    df = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')

    failedL = []
    
    for ind in range(len(df)):

        if 'https://phaster.ca/submissions/' not in str(df.at[ind, 'joblinkforfasta']):
            accnum = df.at[ind, 'accessionNumbers']
            print('{}: {}'.format(ind, accnum))
            job = ''
            newuri = ''

            try:
                bot.get('https://phaster.ca/')
                time.sleep(5)
                inp = bot.find_element_by_xpath('.//input[@id = "submission_sequence"]')
                try:
                    inp.send_keys('C:{}fastafiles/{}.fasta'.format(os.getenv('MAIN_PATH2'), accnum))
                except:
                    raise ValueError
                inp = bot.find_element_by_xpath('.//button[@id = "file-submit"]')
                inp.click()
                time.sleep(2)
                while 'https://phaster.ca/submissions/' not in bot.current_url:
                    continue
                newuri = bot.current_url
                l = newuri.split('/')
                job = l[4]
            except ValueError as e:
                print('File not found!!!')
                failedL.append(accnum)
            except:
                df.at[ind, 'status'] = 'Short'
                pass
            finally:
                df.at[ind, 'jobforfasta'] = job
                df.at[ind, 'joblinkforfasta'] = newuri
                writer = pd.ExcelWriter('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
                df.to_excel(writer, sheet_name = 'Sheet1', index = False)
                writer.save()
                
    time.sleep(4)
    bot.close()
    bot.quit()

    writer = pd.ExcelWriter('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
    
    print(failedL)
