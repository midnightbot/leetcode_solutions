/* The knows API is defined for you.
      bool knows(int a, int b); */

class Solution {
public:
    int findCelebrity(int n) {
        //may exist one celebrity
        // everyone knows the celebrity
        // celebrity does not know anyone of them
        
        for(int x=0;x<n;x++){
            int count = 0;
            
            for(int y=0;y<n;y++){
                
                if(x!=y && knows(y,x) && not knows(x,y)){
                    count+=1;
                }
                
                else if(x==y){
                    count+=1;
                }
                else{
                    break;
                }
                
            }
            if (count ==n){
                return x;
            }
        }
        return -1;
        
    }
};
