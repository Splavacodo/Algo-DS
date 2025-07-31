from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        user_to_websites = defaultdict(list)

        for user, _, site in sorted(zip(timestamp, username, website)):
            user_to_websites[user].append(site)
        
        website_seq_counts = defaultdict(int)

        for websites in user_to_websites.values():
            for seq in self.get_combinations(websites):
                website_seq_counts[seq] += 1
        
        most_visited_seq = ()
        max_count = 0

        for seq, count in website_seq_counts.items():
            if count > max_count or (count == max_count and seq < most_visited_seq):
                most_visited_seq = seq
                max_count = count

        return most_visited_seq
    
    def get_combinations(self, websites: list[str]) -> list[tuple[str]]:
        if len(websites) < 3:
            return set()
        
        website_seq_combinations: set[tuple[str]] = set()

        for i in range(len(websites) - 2):
            for j in range(i + 1, len(websites - 1)):
                for k in range(j + 1, len(websites)):
                    website_seq_combinations.add((websites[i], websites[j], websites[k]))
        
        return website_seq_combinations
