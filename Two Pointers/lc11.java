import java.util.*;

class lc11 {
    public int maxArea(final int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            maxArea = Math.max(maxArea, Math.min(height[left], height[right]) * (right - left));
            if (height[left] <= height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return maxArea;
    }
}