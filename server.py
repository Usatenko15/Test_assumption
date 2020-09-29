import re
import requests
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    """"This is going to be the class that ours will subclass.
    When a request comes in, the BaseHTTPRequestHandler will
    automatically route the request to the appropriate request method
    (either do_GET, do_HEAD or do_POST) which we’ve defined on our
    subclass.

    """

    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        self.respond()

    def handle_http(self, status, content_type):
        """"Use handle_http to send our basic http handlers and then
         return the content.

         """

        self.send_response(status)
        self.send_header('Content - type', content_type)
        self.end_headers()
        a = 'https://dou.ua' + self.path
        return bytes(Server.get_text(a), 'UTF-8')

    def respond(self):
        """"In charge of sending the actual response out."""

        content = self.handle_http(200, 'text / html')
        self.wfile.write(content)

    @staticmethod
    def get_text(url):
        """"Method that add a special character if the word consists of 6
        letters and redirect all links with the domain "dou.ua" to a proxy
        server.

        """

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; '
                                 'rv:80.0) Gecko/20100101 Firefox/80.0'}
        rs = requests.get(url, headers=headers)
        root = BeautifulSoup(rs.content, 'html.parser')
        article = root.find('article')
        # This for is used to redirect all links with the domain "dou.ua"
        # to a proxy server
        for a in root.find_all('a'):
            if a.has_attr('href'):
                a['href'] = a['href'].replace("https://dou.ua",
                                              "http://localhost:8888")
        # this part of code add a special character if the word consists
        # of 6 letters, using regular expression
        if article is not None:
            findtext = article.find_all(text=re.compile('\s(\w{6})\s|'
                                                        '\s(\w{6})\.'))
            for comment in findtext:
                result = re.findall('\s(\w{6})\s', comment)
                result = result + re.findall('\s(\w{6})\.', comment)
                result = list(dict.fromkeys(result))
                fixed_text = comment
                for kil in result:
                    fixed_text = re.sub(kil, kil + '™', fixed_text)
                comment.replace_with(fixed_text)
        return root.prettify()
