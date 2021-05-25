#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import pandas as pd

if __name__ == '__main__':

    load_dotenv()

    df = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH')), sheet_name = 'Sheet1')

    l = df['accessionNumbers'].tolist()
    temp = 0
    l2 = []

    for i in l:
        if 'NZ_' in i:
            i = i.replace('NZ_', '')
            if i in l:
                temp+=1
                l2.append(i)

    l = [i for i in l if i not in l2]

    dfnew = pd.DataFrame({'accessionNumbers': l})
    df = pd.merge(dfnew, df, how = 'left', left_on = 'accessionNumbers', right_on = 'accessionNumbers')

    print(df)
    
    for i in os.listdir('{}phaster/fastafiles/'.format(os.getenv('MAIN_PATH'))):
        j = i.replace('.fna', '')
        if j in l2:
            try:
                os.remove('{}phaster/fastafiles/{}'.format(os.getenv('MAIN_PATH'), i))
            except:
                pass

    for i in os.listdir('{}phaster/intactphages/'.format(os.getenv('MAIN_PATH'))):
        j = i.replace('.fna', '')
        if j in l2:
            try:
                os.remove('{}phaster/intactphages/{}'.format(os.getenv('MAIN_PATH'), i))
            except:
                pass

    for i in os.listdir('{}phaster/intactphagesfasta/'.format(os.getenv('MAIN_PATH'))):
        j = i.replace('.fna', '')
        if j in l2:
            try:
                os.remove('{}phaster/intactphagesfasta/{}'.format(os.getenv('MAIN_PATH'), i))
            except:
                pass

    writer = pd.ExcelWriter('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
    
    for i in os.listdir('{}prohunter/fastafiles/'.format(os.getenv('MAIN_PATH'))):
        j = i.replace('.fasta', '')
        if j in l2:
            try:
                os.remove('{}prohunter/fastafiles/{}'.format(os.getenv('MAIN_PATH'), i))
            except:
                pass

    for i in os.listdir('{}prohunter/gff3files/'.format(os.getenv('MAIN_PATH'))):
        j = i.replace('.gff3', '')
        if j in l2:
            try:
                os.remove('{}prohunter/gff3files/{}'.format(os.getenv('MAIN_PATH'), i))
            except:
                pass

    writer = pd.ExcelWriter('{}prohunter/prophages.xlsx'.format(os.getenv('MAIN_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
