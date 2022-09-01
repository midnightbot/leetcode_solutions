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
    int find_ans(TreeNode* root, int maxs) {
        int ans = 0;
        if (root->val >= maxs) {
            ++ans;
        }
        if (root->right!=nullptr) {
            ans+= find_ans(root->right, max(maxs, root->val));
        }
        if (root->left!=nullptr) {
            ans+= find_ans(root->left, max(maxs, root->val));
        }
        return ans;
    }
    int goodNodes(TreeNode* root) {
        return find_ans(root,-100000);
    }
};
