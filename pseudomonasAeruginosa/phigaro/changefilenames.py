#!usr/bin/env python3

from dotenv import load_dotenv
import os

import pandas as pd

if __name__ == '__main__':

    load_dotenv()
    
    df = pd.read_excel('{}prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    
    for ind in range(len(df)):
        
        i = df.at[ind, 'accessionNumbers']
        print(ind, i)

        if os.path.exists('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH2'), i)):
            for j in os.listdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH2'), i)):
                k = j.replace('.phigaro', '')
                if '.tsv' in j:
                    tempDF = pd.read_csv('{}phigaro/files/{}/{}'.format(os.getenv('MAIN_PATH2'), i, j), delimiter = '\t')
                    df.at[ind, 'total'] = len(tempDF)
                os.rename('{}phigaro/files/{}/{}'.format(os.getenv('MAIN_PATH2'), i, j), '{}phigaro/files/{}/{}'.format(os.getenv('MAIN_PATH2'), i, k))

        else:
            df.at[ind, 'total'] = 0

    writer = pd.ExcelWriter('{}phigaro/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
    