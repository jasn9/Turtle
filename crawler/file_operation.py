
import os
import json
def read_link_file(file_path):
       with open(file_path,'r') as fs:
                #x  = fs.read()
                return json.load(fs)

def add_link(file_path, link, base_dir):
        data = read_link_file(file_path)
        with open(file_path,'w') as fs:
                print(data)
                data['link'][base_dir][link] = 1
                json.dump(data,fs)
                #json.dump({'link':{base_dir : {}}},fs)

#add_link('./link_find.json','jkl','localhost')


#read_link_file('./link_find.json')

