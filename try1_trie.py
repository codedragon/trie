# First version of words method for website, only collects the letters, 
# so spits out ever-larger words as it iterates through the Trie.

from collections import defaultdict
 
class Trie:
    def __init__(self):
        self.root = defaultdict(Trie)
        self.value = None
        self.count = 0
 
    def add(self, s, value):
        """Add the string `s` to the 
        `Trie` and map it to the given value."""
        # for some reason this doesn't add the value 0
        # any other number you use as the input vaule, 
        # that number will be used (haven't tried negatives)
        # but if 0 leaves as None. This is curious, and I 
        # wonder why, but not my biggest headache at the 
        # moment...
        
        head, tail = s[0], s[1:]
        cur_node = self.root[head]
        cur_node.count += 1
        if not tail:
            cur_node.value = value
            return  # No further recursion
        self.root[head].add(tail, value)

    def lookup(self, s, default=None):
        """Look up the value corresponding to 
        the string `s`. Expand the trie to cache the search."""
        head, tail = s[0], s[1:]
        node = self.root[head]
        if tail:
            return node.lookup(tail)
        return node.value or default
 
    def count_prefix(self, s, default=None):
        """Lookup the number of words using a particular prefix."""
        head, tail = s[0], s[1:]
        node = self.root[head]
        if tail:
            return node.count_prefix(tail)
        return node.count or default

    def remove(self, s):
        """Remove the string s from the Trie. 
        Returns *True* if the string was a member."""
        head, tail = s[0], s[1:]
        if head not in self.root:
            return False  # Not contained
        node = self.root[head]
        if tail:
            return node.remove(tail)
        else:
            del node
            return True
 
    def prefix(self, s):
        """Check whether the string `s` is a prefix 
        of some member. Don't expand the trie on negatives (cf.lookup)"""
        if not s:
            return True
        head, tail = s[0], s[1:]
        if head not in self.root:
            return False  # Not contained
        node = self.root[head]
        return node.prefix(tail)

    def max(self, depth = 0):
        """Look for largest common prefix, where max is 
        node.depth * (node.count - 1)"""
        # first get what the max is, then worry about 
        # which prefix this corresponds to.

        node = self.root[0]
        #run_max = 0
        #node = self.root[head]
        #if depth * (count - 1) > run_max:
        #    run_max = depth * (count - 1)
        #return node.max(depth = 

    def words(self, prefix = []):
        """Return an iterator over the items (words) of the 'Trie'."""
        word = False
        for char, node in self.root.iteritems():
            prefix.append(char)
            if node.value:
                yield ''.join(prefix)
            for i in node.words():
                yield i

    def items(self):
        """Return an iterator over the items of the `Trie`."""
        for char, node in self.root.iteritems():
            # node.value is none when not at end of word
            # currently goes down each path until it finds a word, then 
            # starts down another path. Need a way to tell if last word
            #print 'top of function, yielding char,', char
            yield char
            #print 'yielded char,',char
            if node.value:
                print "end of word", node.value
            for i in node.items():
                yield i

