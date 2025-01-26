class Solution:
    def partition(self, s: str) -> list[list[str]]:
        partitions = []
        partition = []

        def find_partitions(idx):
            if idx == len(s):
                partitions.append(partition.copy())
                return
            
            for j in range(idx, len(s)):
                if s[idx:j+1] == s[idx:j+1][::-1]:
                    partition.append(s[idx:j+1])
                    find_partitions(j + 1)
                    partition.pop()
        
        find_partitions(0)
        return partitions