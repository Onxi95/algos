class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var idx = 0

        for (num in nums) {
            if (num != `val`) {
                nums[idx] = num
                idx++
            }
        }

        return idx
    }
}
