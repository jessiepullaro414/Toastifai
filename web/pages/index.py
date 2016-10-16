import tornado.web
from handlers import basic
from fragments import *
class Handler(basic.Handler):
    def getgen(self):
        self.cr()
        h = head.basic(self.yat)
        tl = "<img src='static/toast200.png' style='vertical-align:middle'/>"
        doc, tag, text = self.yat
        with tag("html"):
            doc.asis(h.gen())
            with tag("body"):
                with tag("div", klass="container"):
                    with tag("row"):
                        with tag("center"):
                            with tag("h1"):
                                doc.asis(tl + "ifai!")
                            with tag("div", klass="card white darken-1"):
                                with tag("h3"):
                                    doc.asis("Have you ever wanted perfect {0} without the hassle?".format("<img src='static/logo.png' style='vertical-align:middle'/>"))
                            with tag("div", ("id","toast"), klass="waves-effect waves-light btn brown"):
                                text("Yes!")
                            doc.asis("<br>")
                            with tag("div", klass="cono"):
                                with tag("div", ("id", "wtoast"), klass="image back"):
                                    doc.asis("<img src='static/toast200.png'>")
                                with tag("div", ("id", "toaster"), klass="image fore"):
                                    doc.asis("<img src='static/toaster.png'>")
                            with tag("div", ("style", "margin-top:400px;")):
                                doc.asis("")
                            with tag("div", ("id", "ntd"), ("style", "display:none;")):
                                with tag("h1"):
                                    text("Well now you can have it!")
                                with tag("blockquote"):
                                    text("""
                                    Toastifai is a machine intelligence driven toaster.
                                    Built for ease of use with simple notifications and on the fly 'perfect toast analysis';
                                    Toastifai brings the least scary and most helpful artificial intelligence has to you!
                                    All you need is our toaster!
                                    """)
                                with tag("h3"):
                                    text("Built with:")
                                with tag("div", klass="row"):
                                    with tag("div", klass="col s4"):
                                        with tag("div", klass="card white darken-1"):
                                            doc.asis("<br>")
                                            with tag("h5"):
                                                text("Image recognition:")
                                            with tag("a",("href","https://www.clarifai.com/")):
                                                doc.asis("<img src='http://torontohacker.club/images/clarifai.png' width='200px'/>")
                                            doc.asis("<br>")
                                    with tag("div", klass="col s4"):
                                        with tag("div", klass="card white darken-1"):
                                            doc.asis("<br>")
                                            with tag("h5"):
                                                text("Image capture:")
                                            with tag("a",("href","http://opencv.org/")):
                                                doc.asis("<img src='http://1.bp.blogspot.com/-yvrV6MUueGg/ToICp0YIDPI/AAAAAAAAADg/YKNtJPfx-H8/s1600/OpenCV_Logo.png' width='200px'/>")
                                            doc.asis("<br>")
                                    with tag("div", klass="col s4"):
                                        with tag("div", klass="card white darken-1"):
                                            doc.asis("<br>")
                                            with tag("h5"):
                                                text("Hardware:")
                                            with tag("a",("href","https://www.raspberrypi.org/")):
                                                doc.asis("<img src='https://www.raspberrypi.org/wp-content/uploads/2015/08/raspberry-pi-logo.png' width='200px'/>")
                                            with tag("a",("href","https://www.arduino.cc/")):
                                                doc.asis("<img src='https://pbs.twimg.com/profile_images/378800000704356438/9d19310763171b0d958d23a18b3d7e1c_400x400.png' width='200px'/>")
                                            doc.asis("<br>")
        return doc.getvalue()