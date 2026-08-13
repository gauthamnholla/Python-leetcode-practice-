class Solution:
    def countPairs(self, words: List[str]) -> int:
        counts = Counter()
        for word in words:
            diffs = tuple(
                (ord(word[i]) - ord(word[0]) + 26) % 26 
                for i in range(1, len(word))
            )
            counts[diffs] += 1

        result = 0
        for count in counts.values():
            result += count * (count - 1) // 2

        return result