class HitCounter {
public:
    vector<int> arr;
    HitCounter() {
        arr.clear();
    }
    
    void hit(int timestamp) {
        arr.emplace_back(timestamp);
    }
    
    int getHits(int timestamp) {
        int ans = 0;
        for(int x=arr.size()-1; x>=0; --x) {
            if (timestamp - arr[x] < 300) {
                // cout << x << " ";
                ++ans;
            } else {break;}
        }
        // cout << "\n";
        return ans;
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */
