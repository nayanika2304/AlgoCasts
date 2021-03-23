import collections

class Solution(object):
    def is_cylce_dfs(self,symbol,current_word,start_word,length,visited):
        if length == 1:
            return start_word[0] == current_word[-1]

        visited.add(current_word)
        for neighbor in symbol[current_word[-1]]:
            if neighbor not in visited:
                return self.is_cylce_dfs(symbol,neighbor,start_word,length-1,visited)
        visited.remove(current_word)
        return False
    def chained_words(self,words):
        symbol = collections.defaultdict(list)
        for word in words:
            symbol[word[0]].append(word)
        return self.is_cylce_dfs(symbol,words[0],words[0],len(words),set())

print(Solution().chained_words(['apple','eggs','snack','karat','tuna']))
