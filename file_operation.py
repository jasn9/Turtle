
import os
import json
def read_link_file(file_path):
       with open(file_path,'r') as fs:
                #x  = fs.read()
                return json.load(fs)

def add_link(file_path, link, base_url):
        data = read_link_file(file_path)
        with open(file_path,'w') as fs:
                #print(data)
                
                if base_url in data['link']:
                       data['link'][base_url].append(link)
                else:
                     
                     data['link'][base_url] = [link]
                #print("modeified ",file_path)
                json.dump(data,fs)
                #json.dump({'link':{base_dir : {}}},fs)

def del_link(file_path,link,base_url):
       data = read_link_file(file_path)
       with open(file_path,'w') as fs:
              #print(data,file_path)
              data['link'][base_url].remove(link)
              json.dump(data,fs)

#add_link('./link_find.json','jkl','localhost')


#read_link_file('./link_find.json')
def add_data(file_path):
       with open(file_path,'w') as fs:
              json.dump({'link':{}},fs)
              
