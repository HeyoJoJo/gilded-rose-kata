# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
    
    def test_add_quality_default(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.add_quality(items[0])
        self.assertEquals(1, items[0].quality)

    def test_add_quality_by_non_default_amount(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.add_quality(items[0], 5)
        self.assertEquals(5, items[0].quality)

if __name__ == '__main__':
    unittest.main()
