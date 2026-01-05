class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        for char in set(word1 + word2):
            if abs(freq1[char] - freq2[char]) > 3:
                return False
        return True