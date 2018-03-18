import unittest
from bank_analyzer.Sitereader import getSitehtml
from bank_analyzer.Sitereader import getExRatefromHtml
from bank_analyzer.Sitereader import createExchangeRate

from bank_analyzer.Xmlprocess import getSitesfromXml
from bank_analyzer.Site import Site
import requests


class SitereaderTest(unittest.TestCase):
    def setUp(self):
        self.urls = []
        self.urls.append('/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[1]/table/tbody/tr[1]/td[2]')
        self.urls.append('/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]')
        self.urls.append('/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[1]/table/tbody/tr[3]/td[2]')
        self.urls.append('/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[1]/table/tbody/tr[1]/td[3]')
        self.urls.append('/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[3]')
        self.urls.append('/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[1]/table/tbody/tr[3]/td[3]')

    def test_getSitesfromXml(self):
        sites = getSitesfromXml("../../files/site.xml")
        site = sites[0]
        self.assertEqual(site.site_url, "https://alfabank.ua/")
        self.assertEqual(site.buyUsd_url,
                         self.urls[0])
        self.assertEqual(site.buyEur_url,
                         self.urls[1])
        self.assertEqual(site.buyRub_url,
                         self.urls[2])
        self.assertEqual(site.sellUsd_url,
                         self.urls[3])
        self.assertEqual(site.sellEur_url,
                         self.urls[4])
        self.assertEqual(site.sellRub_url,
                         self.urls[5])

    def test_getSitesfromXmlError(self):
        self.assertRaises(FileNotFoundError, getSitesfromXml, '/nofile.xml')
        self.assertRaises(FileNotFoundError, getSitesfromXml, '')

    def test_getHtml(self):
        self.assertTrue(len(getSitehtml("https://alfabank.ua/")) > 0)
        self.assertTrue(len(getSitehtml("https://github.com")) > 0)
        self.assertRaises(requests.exceptions.ConnectionError, getSitehtml, 'http://dsfds')

    def test_getExRatefromHtml(self):
        html = getSitehtml("https://alfabank.ua/")
        self.assertEqual(getExRatefromHtml(html, self.urls[0]), "26.45")
        self.assertEqual(getExRatefromHtml(html, self.urls[1]), "32.45")
        self.assertEqual(getExRatefromHtml(html, self.urls[2]), "0.442")
        self.assertEqual(getExRatefromHtml(html, self.urls[3]), "26.75")
        self.assertEqual(getExRatefromHtml(html, self.urls[4]), "33.05")
        self.assertEqual(getExRatefromHtml(html, self.urls[5]), "0.472")

    def test_createExchangeRate(self):
        site = Site()
        site.setSiteUrl("https://alfabank.ua/")
        site.setbuyUsd(self.urls[0])
        site.setbuyEur(self.urls[1])
        site.setbuyRub(self.urls[2])
        site.setsellUsd(self.urls[3])
        site.setsellEur(self.urls[4])
        site.setsellRub(self.urls[5])
        expected_exRate = createExchangeRate(site)
        self.assertEqual(expected_exRate.buyUsd, '26.45')
        self.assertEqual(expected_exRate.buyEur, '32.45')
        self.assertEqual(expected_exRate.buyRub, '0.442')
        self.assertEqual(expected_exRate.sellUsd, '26.75')
        self.assertEqual(expected_exRate.sellEur, '33.05')
        self.assertEqual(expected_exRate.sellRub, '0.472')


if __name__ == '__main__':
    unittest.main()
