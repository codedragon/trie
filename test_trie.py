from trie import Trie

mytrie = Trie()
mytrie.add('terrorize',1)
mytrie.add('plant',2)

for letters in mytrie.items():
    print 'letters', letters
