class Solution {
   private:
    void backtrack(int n, int openCount, int closeCount, string currentString,
                   vector<string>& ans) {
        if (openCount == n && closeCount == n) {
            ans.push_back(currentString);
            return;
        }

        if (openCount < n) {
            backtrack(n, openCount + 1, closeCount, currentString + "(", ans);
        }
        if (closeCount < openCount) {
            backtrack(n, openCount, closeCount + 1, currentString + ")", ans);
        }
    }

   public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        backtrack(n, 0, 0, "", ans);
        return ans;
    }
};
