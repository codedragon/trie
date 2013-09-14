from collections import defaultdict
 
class Trie:
    def __init__(self):
        self.root = defaultdict(Trie)
        self.value = None
        self.count = 0
 
    #def __str__(self):
    #    return "Letter: %s" % (self.root[0])

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
        #print 'tail',tail
        cur_node = self.root[head]
        cur_node.count += 1
        if not tail:
            #print 'not tail'
            #print 'return',value
            #print cur_node.value
            #print cur_node.count
            cur_node.value = value
            #print 'new count', cur_node.count
            return  # No further recursion
        #print value
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

    def words(self, path = [], prefix = []):
        """Return an iterator over the items (words) of the 'Trie'."""
        for char, node in self.root.iteritems():
            prefix.append(char)
            path.append(node.count)
            # if there is a node.value, then we are at the end of a word
            # we should subtract 1 word from the node path (1 down, how
            # many to go?!)
            if node.value:
                yield ''.join(prefix)
                #yield ''.join(prefix), node.value
                for x,y in enumerate(path):
                        path[x] = y - 1

            # if we are at the end of a word and the count is 1, 
            # we are at the end of a branch, and it is time to 
            # delete letters back to the last branch we haven't 
            # gone down yet.
            #if word and node.count == 1:
            if node.value and node.count == 1:
                # once a letter hits zero words (in path), we can get
                # get rid it. Search backwards to find all zeros. Shouldn't
                # be any zeros in the beginning of path, but at this point, we
                # know we only want the zeros at the end
                #visited = 0
                #for i in reversed(path):
                #    if i == 0:
                #        visited += 1
                #    else:
                #        break
                #print 'visited',visited
                # visited is how many letters gets us back to last branch
                #if path[-1] == 0:
                    #for j in range(visited):
                for j in range(path.count(0)):
                    #print 'popped loop'
                    del path[-1]
                    del prefix[-1]
                    
            for i in node.words():
                #print 'i',i 
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

