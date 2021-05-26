#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import pandas as pd

if __name__ == '__main__':

    load_dotenv()

    maindf = pd.read_excel('{}prophages.xlsx'.format(os.getenv('BASE_PATH')), sheet_name = 'Sheet1')

    df = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH')), sheet_name = 'Sheet1')
    df = pd.merge(df, maindf, how = 'left', left_on = 'accessionNumbers', right_on = 'accessionNumbers')
    print(len(df), len(df[['sizebp', 'accessionNumbers']].dropna()))
    writer = pd.ExcelWriter('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()

    df = pd.read_excel('{}phigaro/prophages.xlsx'.format(os.getenv('MAIN_PATH')), sheet_name = 'Sheet1')
    df = pd.merge(df, maindf, how = 'left', left_on = 'accessionNumbers', right_on = 'accessionNumbers')
    print(len(df), len(df[['sizebp', 'accessionNumbers']].dropna()))
    writer = pd.ExcelWriter('{}phigaro/prophages.xlsx'.format(os.getenv('MAIN_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()

    df = pd.read_excel('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH')), sheet_name = 'Sheet1')
    df = pd.merge(df, maindf, how = 'left', left_on = 'accessionNumbers', right_on = 'accessionNumbers')
    print(len(df), len(df[['sizebp', 'accessionNumbers']].dropna()))
    writer = pd.ExcelWriter('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()

    df = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    df = pd.merge(df, maindf, how = 'left', left_on = 'accessionNumbers', right_on = 'accessionNumbers')
    print(len(df), len(df[['sizebp', 'accessionNumbers']].dropna()))
    writer = pd.ExcelWriter('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()

    df = pd.read_excel('{}prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    df = pd.merge(df, maindf, how = 'left', left_on = 'accessionNumbers', right_on = 'accessionNumbers')
    print(len(df), len(df[['sizebp', 'accessionNumbers']].dropna()))
    writer = pd.ExcelWriter('{}prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
