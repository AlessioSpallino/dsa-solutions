/*
* @param {TreeNode} p
* @param {TreeNode} q
* @return {boolean}
*/
function isSameTree(p, q) {
    // If both nodes are null, they are identical
    if (p == null && q == null) return true;
    // If one is null and the other is not, they are not identical
    if (p == null || q == null) return false;

    // If the values differ, the trees are not identical
    if (p.val !== q.val) return false;

    return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
}
