class basic:
    def __init__(self, yat):
        self.yat = yat
    def gen(self):
        doc, tag, text = self.yat
        with tag("head"):
            with tag("title"):
                text("Toastifai")
            doc.asis("<link rel=icon type='image/png' href='{0}' />".format("static/logo.png"))
            with open("estatic/css.txt", "r") as ef:
                for res in ef.read().split("\n"):
                    doc.asis("<link rel='stylesheet' href='{0}'>".format(res))
            with open("estatic/js.txt", "r") as jf:
                for res in jf.read().split("\n"):
                    with tag("script", ("src", res)):
                        doc.asis("")
        return doc.getvalue()