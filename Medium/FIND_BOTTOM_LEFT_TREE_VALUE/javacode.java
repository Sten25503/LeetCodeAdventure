class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    /**
     * Finds the value of the bottom-leftmost node in a binary tree using level order traversal.
     * 
     * @param root The root node of the binary tree.
     * @return The value of the bottom-leftmost node.
     */
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        int bottomLeftValue = 0;
        while (!queue.isEmpty()) {
            bottomLeftValue = queue.peek().val;
            for (int i = queue.size(); i > 0; --i) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
        return bottomLeftValue;
    }
}
