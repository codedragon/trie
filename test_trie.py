from trie import Trie

mytrie = Trie()
mytrie.add('terrorize',1)
mytrie.add('plant',2)

for c in mytrie.items():
    print c

