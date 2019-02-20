from urllib.request import urlopen
from urllib import parse
from html.parser import HTMLParser
import file_operation as fo

import json



class Search_page(HTMLParser):
        def __init__(self,base_url):
                super().__init__()
                self.base_url = base_url

        def handle_starttag(self,tag,attrs):
                print("Start tag: ",tag)
                if tag=='a' or tag=='form':
                        print(attrs)
                        for i in range(len(attrs)):
                                if attrs[i][0]=='href' or attrs[i][0]=='action':
                                        val = attrs[i][1]
                                        val = parse.urljoin(self.base_url,val)
                                        print(val)
                                        
                                        
        def handle_endtag(self,tag):
                print("End tag ",tag)
        def handle_data(self,data):
                print("Data ",data)
parser = Search_page('http://localhost:8080/')
response = urlopen('http://localhost:8080/')
if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                #print(json.load(response)
                # if 'Application/json' in content-type
                html_string = html_bytes.decode("utf-8")
                #print(html_string)
                parser.feed(html_string)
                
