public class lc283 {
    public void moveZeroes(int[] nums) {
        int zero = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != 0){
                int tmp = nums[i];
                nums[i] = nums[zero];
                nums[zero] = tmp;
                zero ++;
            }
        }
    }
}
