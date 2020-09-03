/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        if (head == null){
            return null;
        }
        Node dummy = new Node();
        dummy.next = head;
        Node cur = dummy;
        Stack stack = new Stack<>();
        stack.push(head);
        while (!stack.isEmpty()){
            cur.next = (Node) stack.pop();
            cur.child = null;
            cur.next.prev = cur;
            cur = cur.next;

            if (cur.next != null){
                stack.push(cur.next);
            }
            if (cur.child != null){
                stack.push(cur.child);
            }
        }
        dummy.next.prev = null;
        return dummy.next;
    }
}