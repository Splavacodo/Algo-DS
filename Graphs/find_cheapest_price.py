class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices_to_dst = [float('inf') for _ in range(n)]
        prices_to_dst[src] = 0

        for _ in range(k + 1):
            temp_prices = prices_to_dst.copy()

            for source, dest, price in flights:
                if prices_to_dst == float('inf'):
                    continue
                
                if prices_to_dst[source] + price < temp_prices[dest]:
                    temp_prices[dest] = prices_to_dst[source] + price
            
            prices_to_dst = temp_prices

        return -1 if prices_to_dst[dst] == float('inf') else prices_to_dst[dst]
