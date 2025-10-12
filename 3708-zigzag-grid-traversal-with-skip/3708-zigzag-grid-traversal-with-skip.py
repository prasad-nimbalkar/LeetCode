class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        if m == 0:
            return []
        n = len(grid[0])

        result = []
        visit = True

        for i in range(m):
            if i % 2 == 0:
                cols = range(0, n)
            else:
                cols = range(n - 1, -1, -1)

            for j in cols:
                if visit:
                    result.append(grid[i][j])
                visit = not visit
        return result
