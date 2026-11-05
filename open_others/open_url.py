import webbrowser

class Navegador:
    def __init__(self, url):
        self.url = url

    def abrir_site(self):
        webbrowser.open(self.url)
        
            