// Question: https://leetcode.com/problems/arithmetic-subarrays/description/
// Medium

class Solution {
    public Boolean isAirthmetic(int[] array){
        if(array.length < 2){
            return false;
        }
        int delta = array[1] - array[0];
        for(int idx=2; idx < array.length; idx++){
            if(array[idx] - array[idx-1] != delta){
                return false;
            }
        }
        return true;
    }

    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] lbound, int[] rbound) {
        List<Boolean> result = new ArrayList<>(lbound.length);

        for(int idx = 0; idx < lbound.length; idx++){
            int left = lbound[idx];
            int right = rbound[idx];
            int[] subarray = Arrays.copyOfRange(nums, left, right+1);
            Arrays.sort(subarray);
            result.add(isAirthmetic(subarray));
        }

        return result;
    }
}


// November 23, 2023

/* 

# Kunal Wadhwa

*/