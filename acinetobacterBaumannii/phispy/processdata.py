#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import numpy as np
import pandas as pd

if __name__ == '__main__':

    load_dotenv()

    df = pd.read_excel('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH')), sheet_name = 'Sheet1')
    l = df['accessionNumbers'].tolist()

    for ind, i in enumerate(l):
        
        print(ind, i)

        if os.path.exists('{}phispy/files/{}'.format(os.getenv('MAIN_PATH'), i)) == False:

            df.at[ind, 'total'] = 0
            df.at[ind, 'intact'] = 0
            df.at[ind, 'defective'] = 0
            df.at[ind, 'avgRank'] = 0
            df.at[ind, 'status'] = 'inadequate ORFs'

        else:

            if 'prophage_information.tsv' not in os.listdir('{}phispy/files/{}'.format(os.getenv('MAIN_PATH'), i)) or 'prophage.tsv' not in os.listdir('{}phispy/files/{}'.format(os.getenv('MAIN_PATH'), i)):
                df.at[ind, 'total'] = 0
                df.at[ind, 'intact'] = 0
                df.at[ind, 'defective'] = 0
                df.at[ind, 'avgRank'] = 0
                df.at[ind, 'status'] = 'inadequate ORFs'
                os.system('rm -r {}phispy/files/{}'.format(os.getenv('MAIN_PATH'), i))
        
            else:
                df.at[ind, 'avgRank'] = np.max(pd.read_csv('{}phispy/files/{}/prophage_information.tsv'.format(os.getenv('MAIN_PATH'), i), delimiter = '\t')['rank'].tolist())/2
                df.at[ind, 'total'] = len(pd.read_csv('{}phispy/files/{}/prophage.tsv'.format(os.getenv('MAIN_PATH'), i), delimiter = '\t'))
                df.at[ind, 'status'] = 'processed'

                if df.at[ind, 'total'] == 0:
                    df.at[ind, 'intact'] = 0
                    df.at[ind, 'defective'] = 0

    writer = pd.ExcelWriter('{}phispy/prophages.xlsx'.format(os.getenv('MAIN_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
