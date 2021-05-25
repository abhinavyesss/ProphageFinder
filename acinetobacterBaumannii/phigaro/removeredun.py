#!/usr/bin/env python3

from dotenv import load_dotenv
import os

if __name__ == '__main__':

    load_dotenv()

    files = os.listdir('{}phigaro/files'.format(os.getenv('MAIN_PATH')))
    print(files)
    print(len(files))
    for i in files:
        if len(os.listdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH'), i))) == 0:
            os.rmdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH'), i))
        elif len(os.listdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH'), i))) == 1:
            l = os.listdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH'), i))
            for f in l:
                os.remove('{}phigaro/files/{}/{}'.format(os.getenv('MAIN_PATH'), i, f))
            os.rmdir('{}phigaro/files/{}'.format(os.getenv('MAIN_PATH'), i))
