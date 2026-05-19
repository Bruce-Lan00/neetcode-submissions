class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        n = len(nums)
        # 第一层循环：指针 i 从 0 走到倒数第二个位置
        for i in range(n):
            # 第二层循环：指针 j 永远从 i 的下一个位置开始，走到最后一个位置
            for j in range(i + 1, n):
                # 如果这两个位置的数相加等于目标值
                if nums[i] + nums[j] == target:
                    return [i, j]
        #Hashmap