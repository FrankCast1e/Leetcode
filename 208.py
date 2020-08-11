'''
Date: 2020-08-11 11:41:09
LastEditors: FrankCast1e
LastEditTime: 2020-08-11 12:11:31
FilePath: /Leetcode/208.py
'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree_storage = dict()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.tree_storage
        for char in word:
            if char not in temp:
                temp[char] = dict()
                temp[char]['ISWORD'] = False
            temp = temp[char]
        temp['ISWORD'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.tree_storage
        for char in word:
            if char not in temp:
                return False
            else:
                temp = temp[char]
        return temp['ISWORD']

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.tree_storage
        for char in prefix:
            if char not in temp:
                return False
            else:
                temp = temp[char]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")   
print(trie.search("app"))
