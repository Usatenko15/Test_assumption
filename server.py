import re  # is used to find words with 6 letters
import requests  # is used to work with html
from bs4 import BeautifulSoup  # is used to work with text from html
from http.server import BaseHTTPRequestHandler


#  This is going to be the class that ours will subclass.
class Server(BaseHTTPRequestHandler):
    # When a request comes in, the BaseHTTPRequestHandler will automatically route the request to the
    # appropriate request method (either do_GET, do_HEAD or do_POST) which we’ve defined on our subclass
    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        self.respond()

    def do_POST(self):
        return

    # use handle_http to send our basic http handlers and then return the content.
    def handle_http(self, status, content_type):
        self.send_response(status)
        self.send_header('Content - type', content_type)
        self.end_headers()
        a = 'https://dou.ua' + self.path
        return bytes(get_text(a), 'UTF-8')

    #  in charge of sending the actual response out
    def respond(self):
        content = self.handle_http(200, 'text / html')
        self.wfile.write(content)


# method that add a special character if the word consists of 6 letters
# and redirect all links with the domain "dou.ua" to a proxy server
def get_text(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    rs = requests.get(url, headers=headers)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.find('article')
    # This for is used to redirect all links with the domain "dou.ua" to a proxy server
    for a in root.find_all('a'):
        if a.has_attr('href'):
            a['href'] = a['href'].replace("https://dou.ua", "http://localhost:8888")
    # this part of code add a special character if the word consists of 6 letters, using regular expression
    if article is not None:
        findtoure = article.find_all(text=re.compile('\s(\w{6})\s'))
        for comment in findtoure:
            resul = re.findall('\s(\w{6})\s', comment)
            for kil in resul:
                fixed_text = re.sub(kil,kil+'™', comment)
            comment.replace_with(fixed_text)
    return root.prettify()
