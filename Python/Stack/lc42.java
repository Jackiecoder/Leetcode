import java.util.Stack;

public class lc42 {
    public int trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        int totalVolume = 0;
        for (int i = 0; i < height.length; i++){
            int h = height[i];
            while (stack.size() > 1 && h > height[stack.peek()]){
                int bottomIndex = stack.pop();
                int poolVolume = Math.max(0, Math.min(h, height[stack.peek()]) - height[bottomIndex]) * (i - stack.peek() - 1);
                totalVolume += poolVolume;
            }
            stack.push(i);
        }
        return totalVolume;
    }
}
