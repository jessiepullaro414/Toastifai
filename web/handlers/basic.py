import tornado.web
from bs4 import BeautifulSoup
from yattag import Doc

class Handler(tornado.web.RequestHandler):
    def cr(self):
        self.yat = Doc().tagtext()
    def getgen(self):
        return "Hello, world!"
    def get(self):
        soup = BeautifulSoup(self.getgen(), "html.parser")
        self.write(soup.prettify())