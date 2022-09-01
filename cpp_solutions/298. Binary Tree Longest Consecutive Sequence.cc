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
    int max_h = 0;
    
    int find_ans(TreeNode* root, int h, int prev) {
        max_h = max(h, max_h);
        if (root == NULL) {
            return h;
        } 
        if (root->val == prev + 1) {
            return max(find_ans(root->right, h + 1, root->val), find_ans(root->left, h + 1, root->val));
        } else {
            return max(find_ans(root->right, 1, root->val), find_ans(root->left, 1, root->val));
        }
    }
    int longestConsecutive(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        find_ans(root, 1, -100000);
        return max_h;
    }
};
