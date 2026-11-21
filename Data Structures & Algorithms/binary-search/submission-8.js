class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        // given an array of distinct integers `nums`
        // sorted in ascending order, and an integer `target`
        // implement a function to search for `target` within `nums`
        // if it exists, return it's index, otherwise, return -1.

        let l = 0;
        let r = nums.length - 1;

        while (l <= r) {
            let m = Math.floor((l + r)/2);
            const val = nums[m];
            if (val == target) {
                return m;
            } else if (val < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1
    }
}
