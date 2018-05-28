from multiprocessing import Process
from socket import *
import re
import sys

# 静态文件目录
# HTML_ROOT_DIR = "./html"
#
# WSGI_PYTHON_DIR = "./wsgipython"



class HTTPServer(object):
    """http服务器"""

    def __init__(self, application):
        """标准TCP_Server套接字建立"""
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = application

    def start(self):
        """httpserver开始运行"""
        self.server_socket.listen()
        while True:
            # 进程处理client套接字
            cli_socket, cli_info = self.server_socket.accept()
            print('%s %s用户已发送请求' % (cli_info))
            p = Process(target=self.dealClient, args=(cli_socket, cli_info))
            p.start()
            cli_socket.close()

    def start_response(self, status, headers):
        """处理返回状态码和头部信息"""
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers +=  "%s: %s\r\n" % header
        self.response_headers = response_headers

    def dealClient(self, cli_socket, cli_info):
        """处理客户端请求信息 发送数据包
        GET / HTTP/1.1\r\n
        Host: 127.0.0.1:9999\r\n
        Connection: keep-alive\r\n
        Upgrade-Insecure-Requests: 1\r\n
        \r\n"""

        # 接收数据
        rec_data = cli_socket.recv(1024).decode()

        # 提取HTTP报文数据, 提取请求path
        request_lines = rec_data.splitlines()
        request_start_line = request_lines[0]
        file_name = re.match(r'\w+ +(/[^ ]*) ', request_start_line).group(1)
        method = re.match(r'(\w+) +/[^ ]* ', request_start_line).group(1)

        # APPlication 处理路由信息并返回body
        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body

        # 发送数据包
        cli_socket.send(bytes(response, "utf-8"))
        #print(response)
        cli_socket.close()
        print('%s %s用户请求处理完成,已响应' % (cli_info))

    def bind(self, port):
        self.server_socket.bind(('', port))


def main():
    # sys.path.insert(1, WSGI_PYTHON_DIR)

    if len(sys.argv) < 2:
        sys.exit("python MyWebServer.py Module:app")

    module_name, app_name = sys.argv[1].split(":")
    # module_name = MyFrameWork
    # app_name = app
    m = __import__(module_name)
    app= getattr(m, app_name)

    http_server = HTTPServer(app)
    http_server.bind(9999)
    http_server.start()


if __name__ == '__main__':
    main()
