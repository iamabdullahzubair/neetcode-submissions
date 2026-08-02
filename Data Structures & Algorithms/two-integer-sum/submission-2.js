class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map()
        for (let i = 0; i < nums.length; i++) {
            map.set(nums[i], i)
        }
        for (let i = 0; i < nums.length; i++) {
            const remaining = target - nums[i]
            if(map.has(remaining) && map.get(remaining) != i){
                return [i, map.get(remaining)]
            }
        }
    }
}
