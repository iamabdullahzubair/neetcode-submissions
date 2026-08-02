class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        let ans = [];

        function backtrack(openCount, closeCount, currentString) {
            if (openCount == n && closeCount == n) {
                ans.push(currentString);
            }

            if (openCount <= n) {
                backtrack(openCount + 1, closeCount, currentString + "(");
            }
            if (closeCount < openCount) {
                backtrack(openCount, closeCount + 1, currentString + ")");
            }
        }

        backtrack(0, 0, "");
        return ans
    }
}
