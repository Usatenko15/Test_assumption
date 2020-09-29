import time
from http.server import HTTPServer
from server import Server

# define two constants we’ll be using when we launch the server
HOST_NAME = 'localhost'
PORT_NUMBER = 8888

if __name__ == '__main__':
    # create the HTTP object with previous defined parameters
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    # this block actually starts up the server and runs it:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))
