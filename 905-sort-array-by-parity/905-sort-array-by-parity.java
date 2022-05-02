class Solution {
    public int[] sortArrayByParity(int[] nums) {
        ArrayList<Integer> even = new ArrayList();
        ArrayList<Integer> odd = new ArrayList();
        
        for(int i=0; i<nums.length; i++) {
            if(nums[i]%2 == 0) {
                even.add(nums[i]);
            }else {
                odd.add(nums[i]);
            }
        }
        
        even.addAll(odd);
        for(int j=0; j<even.size(); j++){
            nums[j] = even.get(j);
        }
        
        return nums;
    }
}