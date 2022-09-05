/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        if (root == nullptr) {
            return ans;
        }
        vector<Node*> q;
        q.emplace_back(root);
        while(q.size()!=0) {
            vector<int> this_lvl;
            vector<Node*> new_q;
            for(auto it : q) {
                this_lvl.emplace_back(it->val);
                
                for(auto nei : it->children) {
                    new_q.emplace_back(nei);
                }
            }
            q = new_q;
            ans.emplace_back(this_lvl);
        }
        
        return ans;
    }
};
