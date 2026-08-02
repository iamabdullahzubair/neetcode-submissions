class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const str1 = s.split("");
        const str2 = t.split("");

        if (str1.length != str2.length) {
            return false;
        }
        const map = new Map();

        for (const c of str1) {
            if (map.has(c)) {
                map.set(c, map.get(c) + 1);
            } else map.set(c, 1);
        }
        const map2 = new Map();
        for (const c of str2) {
            if (map2.has(c)) {
                map2.set(c, map2.get(c) + 1);
            } else map2.set(c, 1);
        }

        if (map.size != map2.size) {
            return false;
        }

        for (const [key, value] of map) {
            if (!map2.has(key)) {
                return false;
            }

            if (map2.get(key) !== value) {
                return false;
            }
        }

        return true;
    }
}
