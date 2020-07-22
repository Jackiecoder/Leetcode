class Solution {
    public String removeDuplicates(String s, int k) {
        if (s == null || s.length() == 0) {
            return new String();
        }
        Stack<Character> stackChar = new Stack<>();
        Stack<Integer> stackInt = new Stack<>();
        for (char c : s.toCharArray()) {
            if (!stackChar.isEmpty() && stackChar.peek() == c) {
                int times = stackInt.pop();
                if (times + 1 == k) {
                    stackChar.pop();
                } else {
                    stackInt.push(times + 1);
                }
            } else {
                stackChar.push(c);
                stackInt.push(1);
            }
        }
        // System.out.println(stackChar);
        // System.out.println(stackInt);

        StringBuilder sb = new StringBuilder();
        while (!stackChar.isEmpty()) {
            char c = stackChar.pop();
            int times = stackInt.pop();
            String str = Character.toString(c);
            sb.append(str.repeat(times));
        }
        return sb.reverse().toString();
    }
}