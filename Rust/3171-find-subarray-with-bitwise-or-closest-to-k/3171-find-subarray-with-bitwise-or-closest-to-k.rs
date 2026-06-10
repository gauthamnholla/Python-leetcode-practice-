use std::collections::HashSet;
impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut s: HashSet<i32> = HashSet::new();
        let mut dp: Vec<HashSet<i32>> = vec![HashSet::new(); n];
        s.insert(nums[0]);
        dp[0].insert(nums[0]);
        for i in 1..n {
            s.insert(nums[i]);
            dp[i].insert(nums[i]);
            let previous_values = dp[i - 1].clone();
            for x in previous_values {
                let temp = x | nums[i];
                s.insert(temp);
                dp[i].insert(temp);
            }
        }
        let mut ans = i32::MAX;
        for &i in &s {
            ans = ans.min((k - i).abs());
        }
        ans
    }
}