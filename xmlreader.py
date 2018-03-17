import xml.etree.ElementTree as ET
from Site import Site


def getSitesfromXml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    sites = []
    for child in root:
        site = Site()
        for siteinfo in child:
            if siteinfo.tag == "Url":
                site.setSiteUrl(siteinfo.text)
            elif siteinfo.tag == "BuyMoneysUrl":
                for buy in siteinfo:
                    if buy.tag == "USD":
                        site.setbuyUsd(buy.text)
                    elif buy.tag == "EUR":
                        site.setbuyEur(buy.text)
                    elif buy.tag == "RUB":
                        site.setbuyRub(buy.text)
            elif siteinfo.tag == "SellMoneyUrl":
                for sell in siteinfo:
                    if sell.tag == "USD":
                        site.setsellUsd(sell.text)
                    elif sell.tag == "EUR":
                        site.setsellEur(sell.text)
                    elif sell.tag == "RUB":
                        site.setsellRub(sell.text)
        sites.append(site)
    return sites




# n = getSitesfromXml('example.xml')
# for x in n:
#     print(x.sellRub_url)