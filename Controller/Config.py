class ConfigApplication:
    def __init__(self):
        self.icon = None
        self.windowTitle = "Klient Bazy danych"
        self.minimalWindowWidth = 500
        self.minimalWindowHeight = 500

    def getWindowTitle(self):
        return self.windowTitle

    def getMinimalWidth(self):
        return self.minimalWindowWidth

    def getMinimalHeight(self):
        return self.minimalWindowHeight
