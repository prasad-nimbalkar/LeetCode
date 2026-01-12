class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {s: i for i, s in enumerate(list1)}

        min_sum = float("inf")
        result = []

        for j, s in enumerate(list2):
            if s in index_map:
                curr_sum = j + index_map[s]

                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [s]
                elif curr_sum == min_sum:
                    result.append(s)

        return result


# Time: O(n+m)
# Space: O(n)
