#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    load_dotenv()

    maindf = pd.DataFrame()

    df = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    df = df[['accessionNumbers']]
    maindf = maindf.append(df, ignore_index = True)

    df = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH')), sheet_name = 'Sheet1')
    df = df[['accessionNumbers']]
    maindf = maindf.append(df, ignore_index = True)
    
    print(maindf)

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'download.prompt_for_download': False, 'download.directory_upgrade': True})
    bot = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'), options = options)

    for ind in range(len(maindf) - 1, 0, -1):
        
        if maindf.at[ind, 'sizebp'] == 'Hello':
            accnum = maindf.at[ind, 'accessionNumbers']
            print('{}: {}'.format(ind, accnum))
            text = ''

            try:
                bot.get('https://www.ncbi.nlm.nih.gov/nuccore/{}'.format(accnum))
                time.sleep(2)

                while True:

                    try:
                        inp = bot.find_element_by_xpath('.//pre[@class = "genbank"]')
                        l = inp.get_attribute('innerHTML').split(' ')
                        l = [i.strip().replace('\n', '') for i in l if i not in ['', ' ']]
                        print(l[2])
                        maindf.at[ind, 'sizebp'] = l[2]
                        break
                    
                    except KeyboardInterrupt:
                        break

                    except:
                        continue

                time.sleep(1)
                
            except Exception as e:
                pass

            finally:
                writer = pd.ExcelWriter('{}prophages.xlsx'.format(os.getenv('BASE_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
                maindf.to_excel(writer, sheet_name = 'Sheet1', index = False)
                writer.save()
        
    time.sleep(4)
    bot.close()
    bot.quit()

    writer = pd.ExcelWriter('{}prophages.xlsx'.format(os.getenv('BASE_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    maindf.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
