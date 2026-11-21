class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let ourMap = new Map(); // {num:index}

        for (let i = 0; i < nums.length; i++) {
            const need = target - nums[i];
            if (ourMap.has(need)) {
                return [ourMap.get(need),i];
            }
            ourMap.set(nums[i],i);
        }
        
    }
}
