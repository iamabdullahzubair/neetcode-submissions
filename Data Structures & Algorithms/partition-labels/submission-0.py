class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i in range(len(s)):
            mp[s[i]] = i
        groups = []
        start = 0
        end = 0
        # print(mp)
        for i in range(len(s)):
            end = max(end, mp[s[i]])
            # print(i,s[i],end)
            if i == end:
                groups.append(end - start + 1)
                start = i + 1

        return groups