class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        deletions = 0

        for col in range(m):
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    deletions += 1
                    break

        return deletions
