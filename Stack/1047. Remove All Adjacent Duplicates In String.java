import java.util.*;

class Solution {
    public String removeDuplicates(String S) {
        if (S == null || S.length() == 0) {
            return new String();
        }
        Stack<Character> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < S.length(); i++) {
            if (!stack.isEmpty() && stack.peek() == S.charAt(i)) {
                stack.pop();
            } else {
                stack.push(S.charAt(i));
            }
        }
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        return sb.reverse().toString();
    }

    public String removeDuplicates_test(String S) {
        Deque<Character> dq = new ArrayDeque<>();
        for (char c : S.toCharArray()) {
            if (!dq.isEmpty() && dq.peekLast() == c) {
                dq.pollLast();
            } else {
                dq.offer(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char c : dq) {
            sb.append(c);
        }
        return sb.toString();
    }
}