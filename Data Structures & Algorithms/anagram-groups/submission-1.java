class Solution {
    // public String CharSort(String str){
    //     char[] ch = str.toCharArray();
    //     Arrays.sort(ch);
    //     return new String(ch);
    // }
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        for(int i=0;i<strs.length;i++){
            int[] count = new int[26];
            for(char c : strs[i].toCharArray()){
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(strs[i]);
        }

        return new ArrayList(res.values());
    }
    
}
