#!/usr/bin/env python3

from dotenv import load_dotenv
import os

if __name__ == '__main__':

    load_dotenv()

    files = os.listdir('{}phigaro/files'.format(os.getenv('MAIN_PATH2')))
    print(files)
    print(len(files))
    for i in files:
        if len(os.listdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH2'), i))) == 0:
            os.rmdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH2'), i))
        elif len(os.listdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH2'), i))) == 1:
            l = os.listdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH2'), i))
            for f in l:
                os.remove('{}phigaro/files/{}/{}'.format(os.getenv('MAIN_PATH2'), i, f))
            os.rmdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH2'), i))
