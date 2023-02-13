class Solution {
public:
    int countOdds(int low, int high) {

        if(low%2==0 and high%2==0){
            return (int)(high-low)/2;
        }
        else if(low%2==0 and high%2!=0){
            return (int)((high-1-low)/2) + 1;
        }
        else if(low%2!=0 and high%2==0){
            return (int)((high-low-1)/2) + 1;
        }
        else{
            return (int)((high-low)/2) + 1;
        }
        
    }
};
