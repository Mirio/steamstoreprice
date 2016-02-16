# -*- coding: utf-8 -*-
from unittest import TestCase, main
from steamstoreprice import SteamStorePrice


class TestAmazonStorePrice(TestCase):
    def setUp(self):
        self.lib = SteamStorePrice()
        self.urltest = "http://store.steampowered.com/app/349040/"

    def test_normalizeurl(self):
        self.assertEqual(self.lib.normalizeurl(self.urltest), self.urltest)

    def test_normalizeprice(self):
        self.assertEqual(self.lib.normalizeprice("€1,00"), 1.00)
        self.assertEqual(self.lib.normalizeprice("$14.08"), 14.08)
        self.assertEqual(self.lib.normalizeprice("£11.00"), 11.00)

    def test_geturl(self):
        self.assertEqual(self.lib.getpage(self.lib.normalizeurl(self.urltest)).find(
            "div", {"class": "apphub_AppName"}).contents[0], "NARUTO SHIPPUDEN: Ultimate Ninja STORM 4")

    def test_getprice(self):
        self.assertIsInstance(self.lib.getprice(self.urltest), float)

if __name__ == '__main__':
    main(verbosity=3)
