class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        # 2 < 4 > 3 > 2 = 2 < 5 > 1 < 4
        # -------   -     -------------
        #     3     2        4
        #
        # 2 < 4 > 3  -> length = 3
        # 3 > 2     -> same '>' again, so break
        # 2 = 2     -> equal, completely break
        # 2 < 5 > 1 < 4 -> length = 4

        prev = ""
        length = 1
        ans = 1

        for i in range(1, len(arr)):

            if arr[i] < arr[i-1] and prev != "<":
                prev = "<"
                length += 1

            elif arr[i] > arr[i-1] and prev != ">":
                prev = ">"
                length += 1

            else:
                ans = max(ans, length)

                if arr[i] == arr[i - 1]:
                    # 2 = 2
                    # Kuch continue nahi ho sakta
                    length = 1
                    prev = ""

                else:
                    # Same direction:
                    # 3 > 2, previous bhi '>' tha
                    # Purani turbulence break
                    # But 3 > 2 khud length 2 hai
                    length = 2

                    # Current comparison ko next ke liye save karo
                    prev = "<" if arr[i] < arr[i - 1] else ">"

        return max(ans, length)