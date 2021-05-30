#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import pandas as pd

if __name__ == '__main__':

    load_dotenv()

    df = pd.read_excel('{}prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    df = df[['accessionNumbers', 'size', 'strain', 'type']]
    
    tempdf = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    tempdf = pd.merge(tempdf, df, how = 'inner', on = 'accessionNumbers')
    writer = pd.ExcelWriter('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    tempdf.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()

    tempdf = pd.read_excel('{}phigaro/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    tempdf = pd.merge(tempdf, df, how = 'inner', on = 'accessionNumbers')
    writer = pd.ExcelWriter('{}phigaro/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    tempdf.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()

    tempdf = pd.read_excel('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    tempdf = pd.merge(tempdf, df, how = 'inner', on = 'accessionNumbers')
    writer = pd.ExcelWriter('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    tempdf.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
