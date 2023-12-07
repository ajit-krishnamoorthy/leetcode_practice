class Solution:
    def predictPartyVictory(self, senate: str) -> str:
      r_queue = deque()
      d_queue = deque()
      for i in range(len(senate)):
        if senate[i] == 'R':
          r_queue.append(i)
      for i in range(len(senate)):
        if senate[i] == 'D':
          d_queue.append(i)
      while r_queue and d_queue:
        r_fight = r_queue.popleft()
        d_fight = d_queue.popleft()
        if r_fight < d_fight:
          r_queue.append(len(senate)+r_fight)
        else:
          d_queue.append(len(senate)+d_fight)
      return "Radiant" if r_queue else "Dire"