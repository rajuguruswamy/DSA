from typing import List, Set


print("-------------Contains Duplicate------------")


class Solution:
    def hasDupicate_Brute_Force(self, nums: List[int]) -> bool:
        print("1. Brute Force")
        # Time complexity  O(n^2)
        # Space complexity O(1)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def hasDupicate_Sorting(self, nums: List[int]) -> bool:
        print("2. Sorting")
        # Time complexity  O(n log n)
        # Space complexity O(1) or O(n) depending on the sorting algorithm used

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

    def hasDuplicate_Hash_Set(self, nums: List[int]) -> bool:
        print("3. Hash Set")
        # Time complexity  O(n)
        # Space complexity O(n)

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


#  Time complexity can be improved using a hash set
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    nums1 = [1, 2, 3, 4]
    obj = Solution()
    print(obj.hasDupicate_Brute_Force(nums))
    print(obj.hasDupicate_Brute_Force(nums1))
    print(obj.hasDupicate_Sorting(nums))
    print(obj.hasDupicate_Sorting(nums1))
    print(obj.hasDuplicate_Hash_Set(nums))
    print(obj.hasDuplicate_Hash_Set(nums1))
