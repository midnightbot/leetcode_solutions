/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int node_ans(TreeNode* node, set<int> &arrs) {
        if (node->left == nullptr) {
            arrs.insert(node->val);
            return node->val;
        } else {
            node->val = min(node_ans(node->left, arrs),node_ans(node->right, arrs));
            arrs.insert(node->val);
            return min(node_ans(node->left, arrs),node_ans(node->right, arrs));
        }
    }
    int findSecondMinimumValue(TreeNode* root) {
        set<int> nums;
        vector<int> arr;
        int temp = node_ans(root,nums);
        // cout << nums.size();
        for(auto it : nums) {
            arr.emplace_back(it);
        }
        sort(arr.begin(),arr.end());
        if (arr.size() >= 2) {
            return arr[1];
        } else {
            return -1;
        }
    }
};
