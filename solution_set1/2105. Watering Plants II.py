##ss
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        #print(len(plants))
        if len(plants) == 1:
            x=0
            refil = 0
            if capacityA >= capacityB:
                if plants[x] <= capacityA:
                    capacityA-=plants[x]

                else:
                    refil+=1
                    capacityA = og
                    capacityA-=plants[x]
                    
            else:
                if plants[x] <= capacityB:
                    capacityB-=plants[x]

                else:
                    refil+=1
                    capacityB = og1
                    capacityB-=plants[x]
                
            return refil

        elif len(plants)%2==0:
            refil = 0
            og = capacityA
            for x in range(0,len(plants)//2,1):
                #print(x)
                if plants[x] <= capacityA:
                    capacityA-=plants[x]

                else:
                    refil+=1
                    capacityA = og
                    capacityA-=plants[x]

            og = capacityB
            for x in range(len(plants)-1,len(plants)//2-1,-1):
                #print(x,"-")
                if plants[x] <= capacityB:
                    capacityB-=plants[x]

                else:
                    refil+=1
                    capacityB = og
                    capacityB-=plants[x]

            return refil
        
        else:
            
            refil = 0
            og = capacityA
            og1 = capacityB
            for x in range(0,len(plants)//2,1):
                #print(x)
                if plants[x] <= capacityA:
                    capacityA-=plants[x]

                else:
                    refil+=1
                    capacityA = og
                    capacityA-=plants[x]

            og = capacityB
            for x in range(len(plants)-1,len(plants)//2,-1):
                #print(x,"-")
                if plants[x] <= capacityB:
                    capacityB-=plants[x]

                else:
                    refil+=1
                    capacityB = og1
                    capacityB-=plants[x]
                    
            #print(x)
            #print(capacityA, capacityB)
            x = len(plants)//2
            if capacityA >= capacityB:
                if plants[x] <= capacityA:
                    capacityA-=plants[x]

                else:
                    refil+=1
                    capacityA = og
                    capacityA-=plants[x]
                    
            else:
                if plants[x] <= capacityB:
                    capacityB-=plants[x]

                else:
                    refil+=1
                    capacityB = og1
                    capacityB-=plants[x]
                
            return refil
            
