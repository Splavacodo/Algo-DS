from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        num_counts = Counter(hand)
        
        for num in hand:
            start = num
            
            while num_counts[start - 1]:
                start -= 1
            
            while start <= num:
                while num_counts[start]:
                    for next_num in range(start, start + groupSize):
                        if not num_counts[next_num]:
                            return False
                    
                        num_counts[next_num] -= 1

                start += 1
            
        return True