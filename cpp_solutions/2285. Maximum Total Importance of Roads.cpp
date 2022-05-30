//ss
class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        
        unordered_map<int,int> degree;
        vector<pair<int,int>> temp;
        long long ans = 0;
        unordered_map<int,int> imp;
        for(int x =0; x<roads.size();x++){ // indegree found
            if (degree.find(roads[x][0])!=degree.end()){
                degree[roads[x][0]]+=1;
            }
            else{
                degree.insert({roads[x][0],1});
            }
            if (degree.find(roads[x][1])!=degree.end()){
                degree[roads[x][1]]+=1;
            }
            else{
                degree.insert({roads[x][1],1});
            }
            
        }
        
        for(auto& it: degree){ // map to vector
            temp.push_back({it.second,it.first});
        }
        
        // temp - degree,node
        
        std::sort(temp.begin(),temp.end());
        int start = n;
        //cout << temp[0].first << " "<< temp[0].second << "\n";
        //cout << temp[1].first << " "<< temp[1].second << "\n";
       // cout << temp[2].first << " "<< temp[2].second << "\n";
        
        for (int x =temp.size()-1; x>=0;x--){
            imp.insert({temp[x].second,start});
            start-=1;
        }
        
        for(int x=0;x<roads.size();x++){
            ans+= imp[roads[x][0]];
            ans+=imp[roads[x][1]];
        }
        return ans;
        
    }
    
};
