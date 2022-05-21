class Solution {
public:
    unordered_map<int,std::vector<int>> graph;
    unordered_map<int,std::vector<int>> memo;
    
    vector<int> closestNode(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        
        
        vector<int> result(query.size(),0);
        
        for(int x=0 ; x < edges.size();x++){
            int node1 = edges[x][0];
            int node2 = edges[x][1];
            graph[node1].push_back(node2);
            graph[node2].push_back(node1);
        }
        //cout << graph;
        
        // function to find path
        // function to find distance
        //cout << graph[0].size();
        for(int x =0; x<query.size();x++){
            string thispath = findpath(query[x][0], query[x][1]);
            vector<int> all_elems;
            string thisthing = "";
            for(int y=0; y<thispath.length();y++){
                if (thispath.at(y) == ','){
                    all_elems.push_back(stoi(thisthing));
                    thisthing = "";
                }
                else{
                    thisthing+=thispath.at(y);
                }
            }
            
            /////////////////
            if (thisthing!=""){
                all_elems.push_back(stoi(thisthing));
            }
            //////////////////
            vector<int> distances(n,0);
            
            if (memo.find(query[x][2])!=memo.end()){
                int i = 0;
                for (int c: memo.at(query[x][2])){
                 distances[i] = c;
                    i+=1;
                }
                
            }
            else{
                int i = 0;
                for(int c: finddistance(query[x][2],n)){
                 distances[i] = c;
                i+=1;
                }
                memo.insert({query[x][2],distances});
                    
            }
            ////////////////////////////
            int temp = 100000;
            int temp_ans = -1;
            
            for (int nei_node : all_elems){
                //cout << temp << distances[nei_node];
                if (distances[nei_node] < temp){
                    temp = distances[nei_node];
                    temp_ans = nei_node;
                }
                //temp = min(temp, distances[nei_node]);
            }
            result[x] = temp_ans;
            ///////////////////////////
        }
        
        
        return result;
        
    }
    
    string findpath(int start,int end){ // function to find a path form startnode to endnode
        
        queue<int> node;
        queue<string> path;
        //return "anish";
        unordered_set<int> visited;
        
        visited.insert(start);
        node.push(start);
        path.push(std::to_string(start));
        
        if (start == end){
            return std::to_string(start);
        }
        
        while (!node.empty()){
            int currentnode = node.front();
            node.pop();
            string currentpath = path.front();
            path.pop();
            //cout << currentpath << "--" << currentnode << "--" << end << "\n";
            for(int nei: graph[currentnode]){
                //cout << nei << "neis";
                if (visited.find(nei)==visited.end()){
                    if (nei == end){
                        //cout << "inside";
                    return currentpath + "," + std::to_string(nei);
                    
                }
                else{
                    node.push(nei);
                    //cout << currentpath + "," + std::to_string(nei);
                    path.push(currentpath + "," + std::to_string(nei));
                }
                    visited.insert(nei);
                    
                }
                
            }
            
            
        }
        //cout << "here";
        //cout << node.size();
        return std::to_string(start);
        
        //return "anish";
    }
    
    vector<int> finddistance(int startnode,int n){ // function to find distance of all other nodes fromt this startnode
        vector<int> ans(n,-1);
        
        ans[startnode] = 0;
        unordered_set<int> visited;
        queue<int> nds;
        queue<int> dists;
        
        nds.push(startnode);
        dists.push(0);
        visited.insert(startnode);
        
        while(!nds.empty()){
            int thisnode = nds.front();
            int thisdist = dists.front();
            nds.pop();
            dists.pop();
            
            for (int neis: graph[thisnode]){
                if (visited.find(neis) == visited.end()){
                    ans[neis] = thisdist + 1;
                    visited.insert(neis);
                    nds.push(neis);
                    dists.push(thisdist + 1);
                }
            }
        }
        return ans;
        
    }
};
