#!usr/bin/env python3

from dotenv import load_dotenv
import os

import pandas as pd

if __name__ == '__main__':

    load_dotenv()
    
    df = pd.read_excel('{}phaster/prophages.xlsx'.format(os.getenv('MAIN_PATH')), sheet_name = 'Sheet1')
    df = df[['accessionNumbers', 'links', 'size', 'strain', 'type']]
    
    templ = []

    for ind in range(len(df)):
        print(ind, df.at[ind, 'accessionNumbers'])
        if os.path.exists('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH'), df.at[ind, 'accessionNumbers'])):
            df.at[ind, 'seqlength'] = 'normal'
        else:
            df.at[ind, 'seqlength'] = 'small'

    writer = pd.ExcelWriter('{}phigaro/prophages.xlsx'.format(os.getenv('MAIN_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
