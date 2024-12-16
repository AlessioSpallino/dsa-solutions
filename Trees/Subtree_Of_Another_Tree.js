/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// Util function to check if two trees are the same
function isSameTree(s, t) {
    if (s == null && t == null) return true;
    if (s == null || t == null) return false;

    if (s.val !== t.val) return false;

    return this.isSameTree(s.left, t.left) && this.isSameTree(s.right, t.right);
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
function isSubtree(root, subRoot) {
    if (!root) return false

    // when I find a value that matches the initial value of the subRoot, then
    // start checking if the two are identical
    if (root.val == subRoot.val) {
        const result = this.isSameTree(root, subRoot);
        if (result) return true
    }

    return this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot);
}
