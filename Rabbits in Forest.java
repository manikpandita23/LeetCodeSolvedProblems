class Solution {
    public int numRabbits(int[] answers) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int ans:answers){
            frequencyMap.put(ans, frequencyMap.getOrDefault(ans, 0)+1);

        }
        int totalRabbits = 0;
        for (Map.Entry<Integer, Integer>entry:frequencyMap.entrySet()){
            int ans = entry.getKey();
            int count = entry.getValue();
            int groupSize = ans+1;
            int numberOfGroups = (int)Math.ceil((double)count/groupSize);
            totalRabbits += numberOfGroups*groupSize;
        }
        return totalRabbits;
        
    }
}
