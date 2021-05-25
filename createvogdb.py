#!/usr/bin/env python3

import os
from dotenv import load_dotenv

from bs4 import BeautifulSoup as bsp
import pickle
import pandas as pd

if __name__ == '__main__':

    load_dotenv()

    l = pickle.load(open('{}voglist.txt'.format(os.getenv('BASE_PATH')), 'rb'))
    print(len(l))
    mainList = []
    
    for i in l:
        tempList = []
        soup = bsp(i, 'html.parser')
        for j in soup.children:
            try:
                for k in j.children:
                    try:
                        for m in k.children:
                            try:
                                for n in m.children:
                                    print(n)
                            except:
                                tempList.append(m)
                    except:
                        tempList.append(k)
            except:
                tempList.append(j)
        mainList.append(tempList)

    df = pd.DataFrame(mainList, columns = ['VOG number',
                                           'Viral Quotient',
                                           'Host Domain',
                                           'Number of Proteins',
                                           'Number of Genomes',
                                           'Number of known Virus Families',
                                           'Number of Known Virus Genera',
                                           'Protein Annotations',
                                           'Protein Annotations Mapping to POGs 2013'])

    writer = pd.ExcelWriter('{}pVOG.xlsx'.format(os.getenv('BASE_PATH')), engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)
    writer.save()
