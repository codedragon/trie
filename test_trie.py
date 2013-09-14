import unittest
#from try1_trie import Trie
from trie import Trie

class TestWords(unittest.TestCase):
    """Tests for function words"""
    
    def setUp(self):
        unittest.TestCase.setUp(self)

        self.mytrie = Trie()
        self.mytrie.add('ant',1)
        self.mytrie.add('ante',2)
        self.mytrie.add('antic',3)
        self.mytrie.add('antsy',4)
        self.mytrie.add('antse',5)
        self.mytrie.add('ban',6)
        self.mytrie.add('banana',7)

    def test_default_case(self):
        """Test words retrieves all words properly from Trie."""
        expected = ['ante','antic','ant','antsy','antse','banana','ban']
        actual = []
        for words in self.mytrie.words():
            actual.append(words)
        #print 'actual',actual
        #print 'expected',expected
        self.assertTrue(sorted(actual)==sorted(expected))
                
if __name__ == '__main__':
    unittest.main(exit=False)
