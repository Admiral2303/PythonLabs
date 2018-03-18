import requests
import urllib.error
from lxml import html
from ExchangeRate import ExchangeRate
from Xmlprocess import getSitesfromXml
from Xmlprocess import writeSitesToXml


def getSitehtml(url):
    try:
        r = requests.get(url)
    except urllib.error.URLError:
        print('Invalid URL({})'.format(url))
    root = html.fromstring(r.content)
    return root



def getExRatefromHtml(html, xpath):
    obj = html.xpath(xpath)
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
