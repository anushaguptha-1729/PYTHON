class Solution:
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        prev = list(range(len(word2) + 1))

        for i, a in enumerate(word1, 1):
            curr = [i]

            for j, b in enumerate(word2, 1):
                if a == b:
                    curr.append(prev[j - 1])
                else:
                    curr.append(1 + min(
                        prev[j],       # delete
                        curr[j - 1],   # insert
                        prev[j - 1]    # replace
                    ))

            prev = curr

        return prev[-1]