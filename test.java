import java.util.*;

class test{
    public void main(String[] args){
        HashMap<int[], String> memo = new HashMap();
        Mapping(1, 5, "One to Five", memo);
    }
    public String Mapping(int start, int end, String target, HashMap memo){
        int[] array = new int[] {start, end};
        if (memo.containkey(array)) {
            System.out.println(array + " is already in memory!");
            return memo.get(array);
        }
        memo.put(array, target);
        System.out.println("Put " + array + " into memory!");
        return target;
    }
}

