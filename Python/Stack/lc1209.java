import java.util.*;

class lc1209 {
    public String removeDuplicates(final String s, final int k) {
        if (s == null || s.length() == 0) {
            return new String();
        }
        final Stack<Character> stackChar = new Stack<>();
        final Stack<Integer> stackInt = new Stack<>();
        for (final char c : s.toCharArray()) {
            if (!stackChar.isEmpty() && stackChar.peek() == c) {
                final int times = stackInt.pop();
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

        final StringBuilder sb = new StringBuilder();
        while (!stackChar.isEmpty()) {
            final char c = stackChar.pop();
            final int times = stackInt.pop();
            final String str = Character.toString(c);
            sb.append(str.repeat(times));
        }
        return sb.reverse().toString();
    }
}