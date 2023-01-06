class Solution {
public:
    void temp_printer(vector<pair<int,int>> s){
        for(auto it : s){
            cout << it.first << "--" << it.second << "\n";
        }
    }
    static bool custom_sorted(const pair<int,int> &a,
              const pair<int,int> &b)
    {
        if(a.second == b.second){
            return a.first < b.first;
        } else if (a.second!=b.second){
            return a.second > b.second;
        } else{return true;}
    }
    void print_vec(vector<string> s){
        for(auto it : s){
            cout << it << "-";
        }
        cout << "\n";
    }
    vector<string> split_the_string(string s){
        vector<string> ans;
        string this_str = "";
        for(auto it : s){
            if(it!=' '){
                this_str+=string(1,it);
            } else {
                ans.emplace_back(this_str);
                this_str = "";
            }
        }
        ans.emplace_back(this_str);
        //print_vec(ans);
        return ans;
    }
    vector<int> topStudents(vector<string>& positive_feedback, vector<string>& negative_feedback, vector<string>& report, vector<int>& student_id, int k) {

        vector<int> ans;

        map<int,int> points;
        set<string> pos;
        set<string> neg;

        
        for(auto it:positive_feedback){
            pos.insert(it);
        }

        for(auto it : negative_feedback) {
            neg.insert(it);
        }

        for(int x=0; x<report.size();++x){
            string s = report[x];
            //split_the_string(s);
            vector<string> temp = split_the_string(s);
            int score = 0;

            for(auto it : temp){
                if (pos.find(it)!=pos.end()){
                    score+=3;
                }
                else if (neg.find(it)!=neg.end()){
                    --score;
                }
            }
            points[student_id[x]] = score;
        }
        vector<pair<int,int>> comp;
        for(auto it : points){
            pair<int,int> temp;
            temp.first = it.first;
            temp.second = it.second;
            comp.emplace_back(temp);
        }
        //temp_printer(comp);
        //cout << "--" ;
        sort(comp.begin(), comp.end(), custom_sorted);
        //cout << comp[0].first<<" " << comp[0].second;
        int i = 0;
        //temp_printer(comp);
        for(int i=0;i<k;++i){
            ans.emplace_back(comp[i].first);
        }
        return ans;
        
    }
};
