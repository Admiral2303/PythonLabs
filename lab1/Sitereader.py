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
        raise
    # except Exception as error:
    #     print(repr(error))
    root = html.fromstring(r.content)
    return root



def getExRatefromHtml(html, xpath):
    obj = html.xpath(xpath)
    return obj[0].text.strip()


