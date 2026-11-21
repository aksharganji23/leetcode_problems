class Solution {
    public int lengthOfLongestSubstring(String s) {
        ArrayList<Character> arr=new ArrayList<>();
        int count=0;
        int max=0;
        for(int i=0;i<s.length();i++){
            //s.charAt(i);
            if(!arr.contains(s.charAt(i))){
                arr.add(s.charAt(i));
                max=arr.size();
            }
           else{
            int idx=arr.indexOf(s.charAt(i));
                for (int j=0;j<=idx;j++) {
                    arr.remove(0);
                }
                arr.add(s.charAt(i));
                max=arr.size();
            }
             count=Math.max(max,count);
           }

        return count;
    }
}