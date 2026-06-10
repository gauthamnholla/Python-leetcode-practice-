class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            return skills.index(max(skills))
        
        queue = deque(range(n))
        win_count = [0] * n
        
        while True:
            player1 = queue.popleft()
            player2 = queue.popleft()
            
            if skills[player1] > skills[player2]:
                winner, loser = player1, player2
            else:
                winner, loser = player2, player1
            
            queue.append(loser)
            win_count[winner] += 1
            win_count[loser] = 0
            
            if win_count[winner] == k:
                return winner
            
            queue.appendleft(winner)

        