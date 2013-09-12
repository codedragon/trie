import unittest
from trie import Trie

class TestWords(unittest.TestCase):
    """Tests for function words"""
    
    def setUp(self):
        unittest.TestCase.setUp(self)

        self.mytrie = Trie()
        self.mytrie.add('ant',1)
        self.mytrie.add('ante',2)
        self.mytrie.add('antic',3)
        self.mytrie.add('ants',4)
        self.mytrie.add('antsy',5)
        self.mytrie.add('antse',7)
        self.mytrie.add('banana',6)

    def test_default_case(self):
        """Test words retrieves all words properly from Trie."""
        expected = ['ant','ante','antic','ants','antsy','antse','banana']
        actual = []
        for words in self.mytrie.words():
            actual.append(words)
        print actual
        print expected
        self.assertTrue(sorted(actual)==sorted(expected))
                
if __name__ == '__main__':
    unittest.main(exit=False)
