'''
@Date: 2020-07-30 15:04:41
@LastEditors: FrankCast1e
@LastEditTime: 2020-07-30 18:24:54
@FilePath: /LeetCode/139.py
'''
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_word_length = 0
        for word in wordDict:
            if len(word) > max_word_length:
                max_word_length = len(word)
        memo = dict()
        return self.my_word_break(s, wordDict, max_word_length, memo, 0)

    def my_word_break(self, s, worddict, max_len, memo, start_index):
        if start_index >= len(s) :
            return True
        match = False
        for i in range(max_len+1):
            piece = s[start_index: start_index+i]
            if piece in worddict:
                if i in memo:
                    if memo[i]: return True
                else:
                    match = self.my_word_break(s, worddict, max_len, memo, start_index+i)
                    memo[i] = match
                    if match: return True
        memo[start_index] = False
        return False

x = Solution()
print(x.wordBreak(s="applepenapple", wordDict=["apple", "pen","apple"]))