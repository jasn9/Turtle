from urllib.request import urlopen
from urllib import parse
from html.parser import HTMLParser
import file_operation as fo
import json

FILE_PATH_WAIT = './link_find.json'
FILE_PATH_DONE = './Done.json'

class Search_page(HTMLParser):
        def __init__(self,base_url,curr_url):
                super().__init__()
                self.base_url = base_url
                self.curr_url = curr_url

        def handle_starttag(self,tag,attrs):
                #print(self.curr_url)
                       
                #print("Start tag: ",tag)
                if tag=='a' or tag=='form':
                        #print(attrs)
                        for i in range(len(attrs)):
                                if attrs[i][0]=='href':
                                        val = attrs[i][1]
                                        val = parse.urljoin(self.base_url,val)
                                        #print(val)
                                        fo.add_link(FILE_PATH_WAIT,val,self.base_url)
                                      
                                        
                                                               
        #def handle_endtag(self,tag):
        #        print("End tag ",tag)
        #def handle_data(self,data):
        #        print("Data ",data)

def start_loop(curr_url,base_url):
        parser = Search_page(base_url,curr_url)
        response = urlopen(curr_url)
        if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                #print(json.load(response)
                # if 'Application/json' in content-type
                html_string = html_bytes.decode("utf-8")
                fo.del_link(FILE_PATH_WAIT,curr_url,base_url)
                fo.add_link(FILE_PATH_DONE,curr_url,base_url)
                parser.feed(html_string)
                
                

