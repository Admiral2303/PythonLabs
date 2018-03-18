import xml.etree.ElementTree as ET
from Site import Site
from lxml import etree


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

def writeSitesToXml(data, file):
    root = etree.Element("xml")
    doc = etree.SubElement(root, "exchange-courses")
    for i in data:
        bankName = etree.SubElement(doc, "bank")
        etree.SubElement(bankName, "Url").text = i.site_url
        buy = etree.SubElement(bankName, "buy")
        etree.SubElement(buy, "RUB").text = i.buyRub
        etree.SubElement(buy, "EUR").text = i.buyEur
        etree.SubElement(buy, "USD").text = i.buyUsd
        sell = etree.SubElement(bankName, "sell")
        etree.SubElement(sell, "RUB").text = i.sellRub
        etree.SubElement(sell, "EUR").text = i.sellEur
        etree.SubElement(sell, "USD").text = i.sellUsd
    tree = etree.ElementTree(root)
    tree.write(file, pretty_print=True)