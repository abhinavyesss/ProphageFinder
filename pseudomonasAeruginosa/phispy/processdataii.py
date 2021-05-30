#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import numpy as np
import pandas as pd

if __name__ == '__main__':

    load_dotenv()

    df = pd.read_excel('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), sheet_name = 'Sheet1')
    l = df['accessionNumbers'].tolist()

    for ind, i in enumerate(l):
        
        print(ind, i)

        if df.at[ind, 'total'] != 0:

            cordDF = pd.read_csv('{}phispy/files/{}/prophage.tsv'.format(os.getenv('MAIN_PATH2'), i), delimiter = '\t')
            tempL = []
            for j in range(len(cordDF)):
                start = cordDF.at[j, 'Start']
                stop = cordDF.at[j, 'Stop']
                tempDF = pd.read_csv('{}phispy/files/{}/prophage_information.tsv'.format(os.getenv('MAIN_PATH2'), i), delimiter = '\t')
                tempL.append(np.mean(tempDF[(tempDF['start'] >= start) & (tempDF['stop'] <= stop)]['rank'].tolist()))

            x = len([j for j in tempL if j > df.at[ind, 'avgRank']])
            df.at[ind, 'intact'] = x
            df.at[ind, 'defective'] = len(tempL) - x

    writer = pd.ExcelWriter('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH2')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
