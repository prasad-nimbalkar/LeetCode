class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: build requirement frequence
        need = [0] * 26
        for ch in licensePlate:
            if ch.isalpha():
                need[ord(ch.lower()) - ord("a")] += 1
        answer = ""

        # Step 2: check each word
        for word in words:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1

            # Step 3: verify if word satisfies requirements
            valid = True
            for i in range(26):
                if freq[i] < need[i]:
                    valid = False
                    break

            # Step 4: update answer
            if valid:
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer


# Time: O(n*m)
# Space: O(1)
