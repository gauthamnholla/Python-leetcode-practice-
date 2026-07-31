class Solution:                         
    def minimumLengthEncoding(self, words: List[str]) -> int:

        words = sorted(map(lambda x: x[::-1], words))

        ans = len(words[-1])+1

        for i in range(len(words)-1):
            if not words[i+1].startswith(words[i]):
                ans+= len(words[i])+1  

        return ans