class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:


        def find_score(arr):
            score = 0
            arr = [0,0] + arr

            for x in range(2, len(arr)):
                if arr[x-1] == 10 or arr[x-2] == 10:
                    score+=2*arr[x]
                else:
                    score+=arr[x]


            return score


        p1 = find_score(player1)
        p2 = find_score(player2)

        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0
