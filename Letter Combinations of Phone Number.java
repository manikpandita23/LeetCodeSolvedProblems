class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> combinations = new ArrayList<>();
        if (digits.length() == 0) {
            return combinations;
        }
        String[] digitMapping = new String[]{
            "",    
            "",    
            "abc", 
            "def", 
            "ghi", 
            "jkl", 
            "mno", 
            "pqrs",
            "tuv", 
            "wxyz" 
        };
        backtrack(0, new StringBuilder(), digits, digitMapping, combinations);
        return combinations;
    }
    private void backtrack(int index, StringBuilder path, String digits, String[] letters, List<String> combinations) {
        if (path.length() == digits.length()) {
            combinations.add(path.toString());
            return; 
        }
        String possibleLetters = letters[digits.charAt(index) - '0'];
        if (possibleLetters != null) {
            for (int i = 0; i < possibleLetters.length(); i++) {
                path.append(possibleLetters.charAt(i));
                backtrack(index + 1, path, digits, letters, combinations);
                path.deleteCharAt(path.length() - 1);
            }
        }
    }
}
