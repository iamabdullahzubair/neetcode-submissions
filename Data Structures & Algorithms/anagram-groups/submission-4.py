class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature = {}

        for word in strs:
            count = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key in signature:
                signature[key].append(word)
            else:
                signature[key] = [word]
        return list(signature.values())