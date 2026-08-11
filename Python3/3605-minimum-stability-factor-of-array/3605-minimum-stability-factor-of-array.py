class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:

        count1 = 0
        for i in nums:
            if i ==1:
                count1+=1
        if count1 + maxC  >= len(nums):
            return 0

        @cache
        def hcf(x, y):
            return x if not y%x else hcf(y%x, x)

        def check(window_size, maxC, nums):
            idx_mapping = dict()
            for idx, val in enumerate(nums):
                # print(idx, window_size, idx_mapping)
                temp = set()
                temp_window = dict()
                l = idx-window_size+1
                break_outer = 0
                if val >1:
                    for key,val2 in idx_mapping.items():
                        suf_hcf = hcf(val, val2)
                        if suf_hcf >1:
                            if key < l:
                                if not maxC:
                                    return False
                                maxC-=1
                                break_outer =1
                                break
                            if suf_hcf not in temp:
                                temp_window[key] = suf_hcf
                                temp.add(suf_hcf)
                    if not break_outer:
                        if val not in temp:
                            temp.add(val)
                            temp_window[idx] = val
                idx_mapping = temp_window
            return True
        
        low = 1
        high = len(nums)
        while low < high:
            mid = (low+high)//2
            if check(mid, maxC, nums):
                high =  mid
            else:
                low = mid+1
        return low

