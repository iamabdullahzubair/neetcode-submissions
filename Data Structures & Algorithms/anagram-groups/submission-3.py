class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in signature:
                signature[key].append(word)
            else:
                signature[key] = [word]
        return list(signature.values())