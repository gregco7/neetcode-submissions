class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tempnums1 = nums1[::] 

        leftPointer = rightPointer = nums1Pointer = 0

        while ((leftPointer < m) and (rightPointer < n)):
            if (nums2[rightPointer] < tempnums1[leftPointer]):
                nums1[nums1Pointer] = nums2[rightPointer]
                rightPointer += 1
            else:
                #Give the equality case to the left array to ensure stable sorting algorithm
                nums1[nums1Pointer] = tempnums1[leftPointer]
                leftPointer += 1
            
            nums1Pointer += 1
        
        #everything in our output array onwards must equal ...
        nums1[nums1Pointer:] = nums2[rightPointer:] + tempnums1[leftPointer:m]






        