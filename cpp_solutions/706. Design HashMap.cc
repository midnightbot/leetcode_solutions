class MyHashMap {
public:
    map<int, int> maps;
    MyHashMap() {
        maps.clear();
    }
    
    void put(int key, int value) {
        if (maps.find(key) == maps.end()) {
            maps.insert({key,value});
        } else {
            maps[key] = value;
        }
    }
    
    int get(int key) {
        if (maps.find(key)!=maps.end()) {
            return maps[key];
        } else {
            return -1;
        }
    }
    
    void remove(int key) {
        if (maps.find(key)!=maps.end()) {
            maps.erase(key);
        } 
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
