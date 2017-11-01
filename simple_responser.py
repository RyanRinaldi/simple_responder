import socket
import signal
import sys

class Server:

    def start_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print('launching HTTP server on ', self.host, ':', self.port)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
        except Exception as e:
            print('unable to launch HTTP server:', e)

        print('successfully started server on port ', self.port)
        print('press Ctrl+C to shut down the server')
        self._wait_for_connections()

    def shutdown(self):
        s.socket.shutdown(socket.SHUT_RDWR)
        s.socket.close()


    # deprecated
    def build_response(self, response):
        headers = ''
        content = ''
        # with open('response.txt', 'r') as response_file:
        #     lines = response_file.readlines()

        print repr(lines)
        return ''.join(lines)
        headers = lines[:lines.index('\n')]
        headers[-1] = headers[-1].rstrip()
        content = lines[lines.index('\n'):]
        response_headers = ''.join(headers).encode()
        response_content = ''.join(content)
        # print repr('response_headers: \n' + response_headers)
        # print repr('response_content: \n' + response_content)
        return response_headers + '\n\n' + response_content


    def _wait_for_connections(self):
        while True:
            print('Awaiting new connections')
            self.socket.listen(3)
            conn, addr = self.socket.accept()
            # conn - socket to client
            # addr - client's address

            print ('got connection from: ', addr)
            data = conn.recv(1024)
            data_string = bytes.decode(data)
            
            # craft the response

            conn.send(self.server_response)
            print('closing connection')
            conn.close()

    def __init__(self, port = 8000):
        self.host = ''
        self.port = port

def graceful_shutdown(sig, dummy):
    s.shutdown()
    import sys
    sys.exit(1)

def get_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            return ''.join(f.readlines())
    else:
    # copy and paste mode
        response = ''
        last = ''
        count = 0
        while True:
            line = raw_input()
            if last == '' and line == '':
                count += 1
                if count > 5:
                    break
            response += '\n' + line
            last = line
        return response

signal.signal(signal.SIGINT, graceful_shutdown)
s = Server(8000)
s.server_response = get_input()
print(s.server_response)
print('starting web server')
s.start_server()

