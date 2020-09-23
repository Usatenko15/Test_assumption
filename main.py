import time                          # time package simply writes timestamps for when our server goes up or down.
from http.server import HTTPServer   # package contains the HTTP server boilerplate from the Python3 standard library.
from server import Server            # importing a single class, Server from server.py file

# define two constants we’ll be using when we launch the server
HOST_NAME = 'localhost'
PORT_NUMBER = 8888

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)   # create the HTTP object with previous defined parameters
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    # this block actually starts up the server and runs it:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))
