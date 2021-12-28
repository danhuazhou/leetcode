"""
给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。
输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
"""
from typing import List


class Trie:
    """
    字典树（前缀树） 是多叉树
    """

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def dfs(self, word: str, start: int, vis: List[bool]) -> bool:
        if start == len(word):
            return True
        if vis[start]:
            return False
        vis[start] = True
        node = self
        for i in range(start, len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word, i + 1, vis):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        ans = []
        root = Trie()
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0, [False] * len(word)):
                ans.append(word)
            else:
                root.insert(word)
        return ans


"""
1. 对words按字符串长度从小到大排序
2. 遍历每个单词判断是否可以拆分成多个单词 

"""

words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses",
         "rat", "ratcatdogcat"]
res = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]

res = Solution().findAllConcatenatedWordsInADict(words)
print(res)
