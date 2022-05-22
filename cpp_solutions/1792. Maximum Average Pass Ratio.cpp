// Solution1 (TLE)
class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extra) {
        // this is max heap
        priority_queue <vector<double>> q;
        double ans = 0;
        
        for (int x=0; x< classes.size();x++){
            double temp = 0;
            //cout << classes[x][0] / (double)classes[x][1];
            temp = (double)((classes[x][0]+1)/((double)classes[x][1]+1)) - (double)((classes[x][0])/(double)(classes[x][1]));
            
            //temp*=-1;
            //cout << temp<< "\n";
            q.push({temp,(double)classes[x][0],(double)classes[x][1]});
        }
        
        for (int x=0; x<extra;x++){
            vector<double> temp = q.top();
            //cout << temp[0];
            temp[1]+=1;
            temp[2]+=1;
            temp[0] = (double)(((temp[1]+1))/((double)(temp[2]+1))) - (double)(((temp[1]))/((double)(temp[2])));
            q.pop();
            q.push(temp);
        }
        
        int n = q.size();
        
        for(int x=0;x<n;x++){
            vector<double> temps = q.top();
            q.pop();
            //cout << temps[1] << temps[2] << "\n";
            
            ans+= temps[1]/(double)temps[2];
        }
        return ans/(double)(n);
    
        
    }
};
