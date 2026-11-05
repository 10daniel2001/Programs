import webbrowser

class Navegador:
    def __init__(self, url):
        self.url = url

    def abrir_site(self):
        webbrowser.open(self.url)

def main():
    site = Navegador("https://wwww.google.com")
    site.abrir_site


if __name__=="__main__":
    main()                