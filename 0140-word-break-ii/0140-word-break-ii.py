
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            # Reached the end
            if start == len(s):
                return [""]

            # Already calculated
            if start in memo:
                return memo[start]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    remaining = dfs(end)

                    for sentence in remaining:
                        if sentence == "":
                            result.append(word)
                        else:
                            result.append(word + " " + sentence)

            memo[start] = result
            return result

        return dfs(0)

