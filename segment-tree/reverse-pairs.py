from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0] * n  # merge buffer

        def count_cross(l: int, m: int, r: int) -> int:
            """
            Count reverse pairs (i, j) where:
            i in [l, m), j in [m, r), and nums[i] > 2 * nums[j]
            Both halves are already sorted.
            """
            cnt = 0
            j = m
            for i in range(l, m):
                while j < r and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += (j - m)
            return cnt

        def merge(l: int, m: int, r: int) -> None:
            """Merge sorted nums[l:m] and nums[m:r] into nums[l:r]."""
            i, j, t = l, m, l

            while i < m and j < r:
                if nums[i] <= nums[j]:
                    temp[t] = nums[i]
                    i += 1
                else:
                    temp[t] = nums[j]
                    j += 1
                t += 1

            while i < m:
                temp[t] = nums[i]
                i += 1
                t += 1
            while j < r:
                temp[t] = nums[j]
                j += 1
                t += 1

            nums[l:r] = temp[l:r]

        def sort_count(l: int, r: int) -> int:
            """Sort nums[l:r] and return reverse pairs count in this range."""
            if r - l <= 1:
                return 0

            m = (l + r) // 2
            cnt = sort_count(l, m) + sort_count(m, r)
            cnt += count_cross(l, m, r)
            merge(l, m, r)
            return cnt

        return sort_count(0, n)