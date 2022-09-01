class MyHashSet {
public:
    set<int> seen;
    MyHashSet() {
        seen.clear();
    }
    
    void add(int key) {
        seen.insert(key);
    }
    
    void remove(int key) {
        seen.erase(key);
    }
    
    bool contains(int key) {
        return (seen.find(key)!=seen.end());
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
