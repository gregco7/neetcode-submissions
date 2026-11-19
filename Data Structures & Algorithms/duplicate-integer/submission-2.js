class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        /**
         * pseudocode
         * set containing nums
         * iterate over nums
         * if nums in set, return false
         * if nums not in set, continue
         * return true outside of loop
         */
        const mySet = new Set()
        for (const num of nums) {
            if (mySet.has(num)) {
                return true;
            }
            mySet.add(num)
        }
        return false;
    }
}
