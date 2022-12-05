
class TrieNode:

    def __init__(self):
        self.children = {} #K=charechter; V=TrieNode
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word=True

    
    def search(self, word):

        def dfs(j, cur_node):            

            cur = cur_node
            for i in range(j,len(word)):
                w = word[i]
                if w=='.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                nxt = cur.children.get(w,None)
                if not nxt:
                    return False
                cur = nxt

            return cur.word
        
        return dfs(0, self.root)

if __name__=='__main__':
    print ("Start")

    wd = WordDictionary()
    wd.addWord("aba")
    wd.addWord("bamba")
    wd.addWord("absolutely")
    wd.addWord("absorption")
    wd.addWord("abstracted")
    wd.addWord("bandit")
    wd.addWord("swindle")
    wd.addWord("qqq")
     
    word = 'ab.'
    f = wd.search(word)
    print ("f:=",f)

    print ("END")