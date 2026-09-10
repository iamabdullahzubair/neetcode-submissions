class Solution:
    def reorganizeString(self, s: str) -> str:
        table = {}
        for c in s:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        sortedTable = sorted(table.items(), key=lambda x: x[1], reverse=True)
        if sortedTable[0][1] > (len(s) + 1) // 2:
            return ""
        sol = ""
        res = [''] * len(s)
        idx = 0
        for char, count in sortedTable:
            for i in range(count):
                res[idx] = char
                idx += 2
                if idx >= len(s):
                    idx = 1   
        return "".join(res)