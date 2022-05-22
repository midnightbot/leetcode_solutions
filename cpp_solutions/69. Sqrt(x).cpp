//ss
class Solution {
public:
    int mySqrt(int x) {
        
        if (x < 2){
            return x;
        }
        
        int low = 2;
        int high = x/2;
        long nums;
        int mid;
        while (low <= high){
            mid = low + (high - low)/2;
            nums = (long) mid * mid;
            
            if(nums > x){
                high = mid - 1;
            }
            else if(nums < x){
                low = mid + 1;
            }
            else{
                return mid;
            }
            
        }
        return high;
        
    }
};
