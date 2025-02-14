class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # for buy order take smallest sell order
        # for sell order take largest buy order
        # 2 heaps

        buy_heap = [] # max heap
        sell_heap = [] # min heap
        mods = 10**9 + 7
        ans = 0

        for price,amount,ordertype in orders:
            # buy order
            if ordertype == 0:
                if sell_heap:
                    left = amount
                    while left and sell_heap and sell_heap[0][0] <= price:
                        sell_price, sell_quantity = heapq.heappop(sell_heap)
                        if sell_quantity > left:
                            heapq.heappush(sell_heap, (sell_price, sell_quantity-left))
                            left = 0

                        elif sell_quantity == left:
                            left = 0

                        else:
                            left-=sell_quantity
                    if left!=0:
                        heapq.heappush(buy_heap, (-price, left))

                else:
                    heapq.heappush(buy_heap, (-price,amount))

            # sell order
            else:
                if buy_heap:
                    left = amount
                    while left and buy_heap and -buy_heap[0][0] >= price:
                        buy_price, buy_quantity = heapq.heappop(buy_heap)
                        if buy_quantity > left:
                            heapq.heappush(buy_heap, (buy_price, buy_quantity - left))
                            left = 0

                        elif buy_quantity == left:
                            left = 0

                        else:
                            left-=buy_quantity

                    if left!=0:
                        heapq.heappush(sell_heap, (price, left))

                else:
                    heapq.heappush(sell_heap, (price, amount))

            # print(buy_heap, sell_heap)
        for x,y in buy_heap:
            ans+=y
            ans%=mods

        for x,y in sell_heap:
            ans+=y
            ans%=mods

        return ans
        
