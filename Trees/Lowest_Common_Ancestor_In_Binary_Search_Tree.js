/**
* @param {TreeNode} root
* @param {TreeNode} p
* @param {TreeNode} q
* @return {TreeNode}
*/
function lowestCommonAncestor(root, p, q) {
    if (p.val == root.val || q.val == root.val) return root;

    if (p.val < root.val && q.val > root.val) return root;
    if (p.val > root.val && q.val < root.val) return root;

    if (p.val <= root.val && q.val <= root.val) {
        return this.lowestCommonAncestor(root.left, p, q);
    }
    if (p.val >= root.val && q.val >= root.val) {
        return this.lowestCommonAncestor(root.right, p, q);
    }
}
