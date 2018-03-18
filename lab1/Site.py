class Site:
    def __init__(self):
        site_url = ""
        buyUsd_url = 0.0
        buyEur_url = 0.0
        buyRub_url = 0.0
        sellUsd_url = 0.0
        sellEur_url = 0.0
        sellRub_url = 0.0

    def setSiteUrl(self, data):
        self.site_url = data

    def setbuyUsd(self, data):
        self.buyUsd_url = data

    def setbuyEur(self, data):
        self.buyEur_url = data

    def setbuyRub(self, data):
        self.buyRub_url = data

    def setsellUsd(self, data):
        self.sellUsd_url = data

    def setsellEur(self, data):
        self.sellEur_url = data

    def setsellRub(self, data):
        self.sellRub_url = data
