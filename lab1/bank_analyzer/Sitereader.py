import requests
import urllib.error
from lxml import html
from bank_analyzer.ExchangeRate import ExchangeRate
from bank_analyzer.Xmlprocess import getSitesfromXml
from bank_analyzer.Xmlprocess import writeSitesToXml


def getSitehtml(url):
    root = ""
    try:
        r = requests.get(url)
        root = html.fromstring(r.content)
    except urllib.error.URLError:
        print('Invalid URL({})'.format(url))
        raise
    return root


def getExRatefromHtml(html, xpath):
    obj = ''
    try:
        obj = html.xpath(xpath)
    except RuntimeError:
        print("Html or xpath incorrect")
    return obj[0].text.strip()


def createExchangeRate(site):
    html = getSitehtml(site.site_url)
    ex_rate = ExchangeRate(site.site_url,
                           getExRatefromHtml(html, site.buyUsd_url),
                           getExRatefromHtml(html, site.buyEur_url),
                           getExRatefromHtml(html, site.buyRub_url),
                           getExRatefromHtml(html, site.sellUsd_url),
                           getExRatefromHtml(html, site.sellEur_url),
                           getExRatefromHtml(html, site.sellRub_url))
    return ex_rate


# exs = []
# for ex in getSitesfromXml("./files/example.xml"):
#     ex1 = createExchangeRate(ex)
#     exs.append(ex1)
#
# writeSitesToXml(exs, "./files/res1.xml")
