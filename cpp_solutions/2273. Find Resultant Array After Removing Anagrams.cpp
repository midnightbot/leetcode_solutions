class Solution {
public:
    bool check(string word1, string word2){ // function to check if two words are anangram
        vector<int> comp1(26,0);
        vector<int> comp2(26,0);
        
        for(int x=0; x<word1.length();x++){
            //cout << (int)word1[x]<<"\n";
            comp1[(int)word1[x] - (int)'a']++;
            
        }
        for(int x=0; x<word2.length();x++){
            //cout << (int)word1[x]<<"\n";
            comp2[(int)word2[x] - (int)'a']++;
            
        }
        
        
        for(int x=0;x<26;x++){
            if (comp1[x]!=comp2[x]){
                return false;
            }
        }
        return true;
    }
    vector<string> removeAnagrams(vector<string>& words) {
        stack<string> stack;
        
        stack.push(words[0]);
        for (int x=1;x<words.size();x++){
            if (stack.empty()){
                stack.push(words[x]);
            }
            else if(not stack.empty() and not check(stack.top(),words[x])){
                stack.push(words[x]);
            }
        }
        
        // below part is to convert stack to vector
        
        int n = stack.size();
        vector<string> ans(n);
        
        for (int x=n-1;x>=0;x--){
            string temp = stack.top();
            stack.pop();
            //cout << temp;
            ans[x] = temp;
        }
        return ans;
    }
};
