import unittest
import Player
class PlayerTest(unittest.TestCase):
    
    def testName(selt):
        name = "A"
        playerA = Player.Player(name)
        
        self.assertEqual(name, playerA.get_name())
        
    def testHand(self):
        playerA = Player.Player("A")
        
        self.assertTrue(0 <= playerA.show_hand() <= 2)
        
    def testWincount(self):
        playerA = Player("A")
        
        playerA.notify_result(True)
        self.assertEqual(1, playerA.get_wincount())
        playerA.notify_result(False)
        self.assertEqual(1, playerA.get_wincount())
    
    
if __name__ == '__main__':
    #import sys:sys.argv = [‘’, ‘Test.testPlayer’]
    unittest.main()