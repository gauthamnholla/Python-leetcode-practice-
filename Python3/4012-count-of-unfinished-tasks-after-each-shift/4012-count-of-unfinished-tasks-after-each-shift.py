class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:

        # Convert tasks into prefix sums so that tasks[i]
        # represents total time required to finish tasks[0...i].
        for i in range(1, len(tasks)):
            tasks[i] += tasks[i - 1]

        # Binary search for the first task that cannot be
        # completely finished in the current shift.
        def bs(shift, offset, left, right):
            while left < right:
                mid = (left + right) // 2

                # Remaining work needed to reach task 'mid'
                required = tasks[mid] - offset

                if required == shift:
                    return mid
                elif required > shift:
                    right = mid
                else:
                    left = mid + 1

            return left

        # Total work already completed before the current task.
        offset = 0

        # Index of the task where the next shift starts.
        left = 0

        right = len(tasks)
        ans = []

        for shift in shifts:

            # Find the first unfinished task after this shift.
            done = bs(shift, offset, left, right)

            # Case 1:
            # All tasks are completed, so restart from task 0.
            if done == right or (done == right - 1 and tasks[done] - offset == shift):
                ans.append(0)
                offset = 0
                left = 0

            # Case 2:
            # A task finishes exactly at the end of the shift.
            elif tasks[done] - offset == shift:
                ans.append(right - done - 1)
                left = done + 1
                offset += shift

            # Case 3:
            # Current task is only partially completed.
            else:
                ans.append(right - done)
                left = done
                offset += shift

        return ans