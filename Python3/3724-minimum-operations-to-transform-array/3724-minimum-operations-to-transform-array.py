class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        val = []
        for i in range(0, n1):
            val.append((min(nums1[i], nums2[i]), max(nums1[i], nums2[i])))
            res += abs(nums1[i] - nums2[i])
        val.sort()
        k=[]
        for i in range(0,len(val)):
            if(len(k)!=0):
                v=k[-1]
                if(v[1]>=val[i][0]):
                    k.pop()
                    m=max(v[1],val[i][1])
                    k.append([v[0],m])
                else:
                    k.append(val[i])
            else:
                k.append(val[i])
        val=k
        for i in range(n1, n2):
            mindiff = float('inf')
            low, high = 0, len(val) - 1
            while low <= high:
                mid = low + (high - low) // 2
                print(mid)
                a, b = val[mid]
                if a <= nums2[i] <= b:
                    mindiff = 0
                    break
                if abs(a - nums2[i]) >= abs(b - nums2[i]):
                    mindiff = min(mindiff,abs(b - nums2[i]))
                    low = mid + 1
                else:
                    mindiff = min(mindiff,abs(a - nums2[i]))
                    high = mid - 1
            print(mindiff)
            res += mindiff
        return res+abs(n1-n2)