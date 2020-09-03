/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n <= 0){
            return new ArrayList<TreeNode>();
        }
        HashMap<int[], List<TreeNode>> memo= new HashMap<>();
        return generateSubtrees(1, n, memo);
    }

    public List<TreeNode> generateSubtrees(int start, int end, HashMap memo){
        int[] array = new int[]{start, end};
        if (memo.containsKey(array)){
            return (List<TreeNode>) memo.get(array);
        }
        List <TreeNode> result = new ArrayList<TreeNode>();
        if (start > end){
            result.add(null);
            return result;
        }
        for (int i = start; i <= end; i ++){
            List <TreeNode> leftSubtrees = generateSubtrees(start, i - 1, memo);
            List <TreeNode> rightSubtrees = generateSubtrees(i + 1, end, memo);
            for (TreeNode leftSubtree: leftSubtrees){
                for (TreeNode rightSubtree: rightSubtrees){
                    TreeNode root = new TreeNode(i, leftSubtree, rightSubtree);
                    result.add(root);
                }
            }
        }
        memo.put(array, result);
        return result;
    }
}

