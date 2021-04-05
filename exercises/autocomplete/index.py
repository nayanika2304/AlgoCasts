class Node:
    def __init__(self,isWord,children):
        self.isWord = isWord
        # {'a':Node,'b':Node...}
        self.children = children

class Solution(object):
    def build(self,words):
        trie = Node(False,{})
        for word in words:
            current = trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node(False,{})
                current = current.children[char]
                current.isWord = True
        self.trie = trie

    def autocomplete(self,word):
        current = self.trie
        for char in word:
            if not char in current.children:
                return []
            current = current.children[char]

        words = []
        self.dfs(current,word,words)
        return []

    def dfs(self,node,prefix,words):
        if node.isWord:
            words.append(prefix)
        for char in node.children:
            self.dfs(node.children[char],prefix + char,words)

    def dfsIterative(self,node,prefix,words):
        stack = [(node,prefix)]
        while len(stack):
            (node,prefix) = stack.pop()
            if node.isWord:
                words.append(prefix)
            for char in node.children:
                child = node.children[char]
                stack.append((child,child+prefix))
        return stack

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']
