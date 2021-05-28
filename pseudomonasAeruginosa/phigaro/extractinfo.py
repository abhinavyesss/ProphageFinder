#!usr/bin/env python3

from dotenv import load_dotenv
import os

import pandas as pd

if __name__ == '__main__':

    load_dotenv()
    
    df = pd.read_excel('{}prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')

    for ind in range(len(df)):
        acc = df.at[ind, 'accessionNumbers']
        print(ind, acc)
        tsvfile = '{}phigaro/files/{}/{}.tsv'.format(os.getenv('MAIN_PATH2'), acc, acc)
        if os.path.exists(tsvfile):
            tempDF = pd.read_csv(tsvfile, delimiter = '\t')
            trans = tempDF['transposable'].tolist()
            tax = tempDF['taxonomy'].tolist()

            if len(tax)>0:
                for i in list(set(tax)):
                    df.at[ind, 'taxonomy_{}'.format(i)] = tax.count(i)

            if len(trans)>0:
                for i in list(set(trans)):
                    df.at[ind, 'transposable_{}'.format(i)] = trans.count(i)

            df.at[ind, 'total'] = len(tempDF)

    df = df.fillna(0)
    l = sorted(list(df.columns))
    df = df[l]

    writer = pd.ExcelWriter('{}phigaro/prophages2.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
