import tornado.ioloop
import tornado.web
from pages import *

def make_app():
    return tornado.web.Application([
        (r"/", index.Handler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path":"static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()