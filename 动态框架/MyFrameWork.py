import time
# from MyWebServer import HTTPServer

HTML_ROOT_DIR = "./static"

class Application(object):
    """框架核心, 路由寻找, 返回404"""
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")

        # 访问静态文件
        if path.startswith("/static"):
            file_name = path[7:]
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                status = "404 Not Found"
                headers = [
                    ("Content-Type", "text/plain"),
                    ("cui_zhen_yu", "da_sha_*"),
                    ("cui_zhen_yu", "da_sha_*"),
                    ("cui_zhen_yu", "da_sha_*"),
                    ("cui_zhen_yu", "da_sha_*"),
                    ("cui_zhen_yu", "da_sha_*")
                ]
                start_response(status, headers)
                return "not foundDdDdD"
            else:
                file_data = file.read()
                file.close()

                status = "200 OK"
                headers = [
                    ("Content-Type", "text/html;charset=utf-8"),
                    ("bu_zhi_dao", "sui_bian")
                ]
                start_response(status, headers)
                return file_data.decode("utf-8")

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)

        # 未找到路由 404
        status = "404 Not Found"
        headers = [
            ("Content-Type", "text/plain"),
            ("cui_zhen_yu", "da_sha_*"),
            ("cui_zhen_yu", "da_sha_*"),
            ("cui_zhen_yu", "da_sha_*"),
            ("cui_zhen_yu", "da_sha_*"),
            ("cui_zhen_yu", "da_sha_*")
        ]
        start_response(status, headers)
        return "not foundDdDdD"


def show_ctime(env, start_response):
    status = "200 ok"
    headers = [
        ("Content-Type", "text/plain"),
        ("bu_zhi_dao", "sui_bian")
    ]
    start_response(status, headers)
    return time.ctime()

def say_hello(env, start_response):
    status = "200 ok"
    headers = [
        ("Content-Type", "text/plain"),
        ("bu_zhi_dao", "sui_bian")
    ]
    start_response(status, headers)
    return "hello, mysay_hello"

urls = [
        ("/", show_ctime),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
    ]

app = Application(urls)

# if __name__ == '__main__':
#
#     urls = [
#         ("/", show_ctime),
#         ("/ctime", show_ctime),
#         ("/sayhello", say_hello)
#     ]
#
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()

