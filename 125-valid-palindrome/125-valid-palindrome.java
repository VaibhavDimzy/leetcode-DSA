class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 0) return true;
        StringBuilder str = new StringBuilder();
        
        for(char c: s.toCharArray()) {
            if((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                str.append(Character.toLowerCase(c));
            }
        }
        // System.out.println(str);
        
        s = new String(str);
        if(s.length() == 0) return true;
        int start=0, end=s.length()-1;
        return helper(s, start,  end);
        
        
    }
    public  boolean helper(String s, int start, int end){
        if(start>=end) return true;
        
        boolean palindrome = helper(s,start+1,end-1);
        if(palindrome == true){
            if(s.charAt(start) == s.charAt(end)) {
                return true;
            } else {
                return false;
            }
        }
        else
            return false;
        
    }
}