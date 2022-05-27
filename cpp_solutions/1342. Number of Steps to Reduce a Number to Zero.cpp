class Solution {
public:
    int numberOfSteps(int num) {
        
        int steps = 0;
        
        while(num!=0){
            steps+=1;
            if (num%2==0){
                num = num/2;
            }
            else{
                num-=1;
            }
        }
        return steps;
        
    }
};
