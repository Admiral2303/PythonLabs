class ExchangeRate:
    def __init__(self, url, buyusd, buyeur, buyrub, sellusd, selleur, sellrub):
        self.site_url = url
        self.buyUsd = buyusd
        self.buyEur = buyeur
        self.buyRub = buyrub
        self.sellUsd = sellusd
        self.sellEur = selleur
        self.sellRub = sellrub
