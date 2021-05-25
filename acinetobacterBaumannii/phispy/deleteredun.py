#!/usr/bin/env python3

from dotenv import load_dotenv
import os

if __name__ == '__main__':
    
    load_dotenv()
    
    l = os.listdir('{}phispy/files'.format(os.getenv('MAIN_PATH')))

    for i in l:
        for j in os.listdir('{}/phispy/files/{}'.format(os.getenv('MAIN_PATH'), i)):
            if '.log' in j or '.gbk' in j or '.tbl' in j or 'prophage_coordinates.tsv' in j:
                os.remove('{}phispy/files/{}/{}'.format(os.getenv('MAIN_PATH'), i, j))
