# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, CommonItem

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

    def test_remove_quality_default(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.decrease_quality(items[0])
        self.assertEquals(9, items[0].quality)

    def test_remove_quality_default(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.decrease_quality(items[0], 5)
        self.assertEquals(5, items[0].quality)

    def test_can_create_common_item(self):
        items = [CommonItem("Health Potion(medium)"), 10, 10]
        self.assertEquals(CommonItem.__class__, type items[0])

if __name__ == '__main__':
    unittest.main()
