#include <numeric>
class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        int eng = 0;
        int exp = 0;
        
        // energy training
        if (accumulate(energy.begin(),energy.end(),0) < initialEnergy) {
            eng = 0;
        } else {
            eng+= accumulate(energy.begin(),energy.end(),0) - initialEnergy + 1;
        }
        
        // experience training
        for (auto it : experience) {
            if (it < initialExperience) {
                initialExperience+=it;
            } else {
                exp+=it - initialExperience+1;
                initialExperience += it - initialExperience + 1;
                initialExperience+= it;
            }
        }
        
        
        
        return eng + exp;
        
    }
};
