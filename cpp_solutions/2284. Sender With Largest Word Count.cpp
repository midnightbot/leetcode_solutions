class Solution {
public:
    string largestWordCount(vector<string>& messages, vector<string>& senders) {
        
        unordered_map<string,int> freq;
        int largest = -1;
        string ans = "";
        for(int x=0;x<messages.size();x++){
            int count = 0;
            for(int y =0;y<messages[x].length();y++){
                if ((int)messages[x].at(y) == 32){
                    count+=1;
                    //cout << count;
                }
            }
            count+=1;
            if (freq.find(senders[x])!=freq.end()){
                freq[senders[x]]+=count;
            }
            else{
                freq.insert({senders[x],count});
            }
        }
        
        for(auto& it : freq){
            //cout << it;
            //cout << freq[(string)it];
            //cout << freq[it.first] <<" " <<it.first << "\n" ;
            if (it.second > largest){
                largest = it.second;
                ans = it.first;
            }
            else if(it.second == largest and (it.first) > (ans)){
                ans = it.first;
            }
        }
        return ans;
        
    }
    
  
};
