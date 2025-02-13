import unittest
from loot_generator import generate_loot, common_loot

class TestLootGenerator(unittest.TestCase):
    def test_generate_loot(self):
        # Test that a loot item is generated from the common_loot list.
        loot = generate_loot(common_loot)
        self.assertIn(loot, common_loot)

    def test_generate_loot_rare(self):
        # Test that a loot item is generated from the rare_loot list
        loot = generate_loot(rare_loot)
        self.assertIn(loot, rare_loot)
    
    def test_generate_specific_loot_weapon(self):
      #Test that the specific loot generated is correct.
      loot = generate_specific_loot(common_loot, "weapon")
      self.assertIn(loot, common_loot)

    def test_generate_specific_loot_armor(self):
      loot = generate_specific_loot(common_loot, "armor")
      self.assertIn(loot, common_loot)
