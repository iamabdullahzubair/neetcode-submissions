class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        # 2<4>3>2=2<5>1<4
        # -----   -------
        prev = ""
        length = 1
        ans = 1
        for i in range(1, len(arr)):

            if arr[i] < arr[i-1] and prev != "<":
                prev = "<"
                length +=1
            elif arr[i] > arr[i-1] and prev != ">":
                prev = ">"
                length +=1
            else:
                ans = max(ans, length)

                if arr[i] == arr[i - 1]:
                    # Equal → kuch bhi continue nahi ho sakta
                    length = 1
                    prev = ""

                else:
                    # Current pair se nayi turbulence start ho sakti hai
                    length = 2

                    # Current comparison ko next iteration ke liye yaad rakho
                    prev = "<" if arr[i] < arr[i - 1] else ">"
        return max(ans, length)

            


            