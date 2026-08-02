class Solution {
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        const freq = new Map();

        for (const c of s) {
            freq.set(c, (freq.get(c) || 0) + 1);
        }

        for (const c of t) {
            if (!freq.has(c)) {
                return false;
            }

            freq.set(c, freq.get(c) - 1);

            if (freq.get(c) === 0) {
                freq.delete(c);
            }
        }

        return freq.size === 0;
    }
}