from trie import Trie

mytrie = Trie()
#mytrie.add('plant',1)
mytrie.add('ant',1)
mytrie.add('ante',2)
mytrie.add('antic',3)
mytrie.add('ants',4)
mytrie.add('antsy',5)
mytrie.add('antse',7)
mytrie.add('banana',6)

for words in mytrie.words():
    print 'WORD',words

