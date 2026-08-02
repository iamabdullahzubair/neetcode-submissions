class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const set = new Map();
        for(const n of nums){
            if(set.has(n)){
                return true
            }
            set.set(n, n)
        }
        return false
    }
}
