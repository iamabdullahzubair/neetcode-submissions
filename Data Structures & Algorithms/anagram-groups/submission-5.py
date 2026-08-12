class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1

            # defaultdict ki wajah se if-else ki zaroorat nahi hai
            signature[tuple(count)].append(word)
        return list(signature.values())
