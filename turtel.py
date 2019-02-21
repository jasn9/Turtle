import file_operation as fo
import json

import looping as loop

BASE_URL = 'http://localhost:8080/'


FILE_PATH_WAIT = './link_find.json'
FILE_PATH_DONE = './Done.json'

def load_turtle():
    fo.add_data(FILE_PATH_WAIT)
    fo.add_data(FILE_PATH_DONE)
    fo.add_link(FILE_PATH_WAIT,BASE_URL,BASE_URL)

def start_turtle():
    while True:
        data = fo.read_link_file(FILE_PATH_WAIT)
        if len(data['link'][BASE_URL])==0:
            print('Crawl Complete')
            break
        else:
            loop.start_loop(data['link'][BASE_URL][0],BASE_URL)
    
load_turtle()
start_turtle()
