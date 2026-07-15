class Solution:
    def resultArray(self, nums):
        a, b = SortedList([nums[0]]), SortedList([nums[1]])
        arr1, arr2 = [nums[0]], [nums[1]]

        for i in range(2, len(nums)):
            x1 = len(a) - a.bisect_right(nums[i])
            x2 = len(b) - b.bisect_right(nums[i])

            if x1 > x2:
                a.add(nums[i])
                arr1.append(nums[i])
            elif x1 < x2:
                b.add(nums[i])
                arr2.append(nums[i])
            elif len(a) > len(b):
                b.add(nums[i])
                arr2.append(nums[i])
            else:
                a.add(nums[i])
                arr1.append(nums[i])

        return arr1 + arr2