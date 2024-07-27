import java.util.*;
class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        if (source.length() != target.length()) {
            return -1;
        }
        Map<Character, List<int[]>> graph = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            graph.put((char) ('a' + i), new ArrayList<>());
        }  
        for (int i = 0; i < original.length; i++) {
            graph.get(original[i]).add(new int[] {changed[i], cost[i]});
        }
        Map<Character, Map<Character, Long>> minCost = new HashMap<>();
        for (char start = 'a'; start <= 'z'; start++) {
            minCost.put(start, dijkstra(start, graph));
        }
        long totalCost = 0;
        for (int i = 0; i < source.length(); i++) {
            char s = source.charAt(i);
            char t = target.charAt(i);
            if (s == t) continue;
            if (minCost.get(s).get(t) == Long.MAX_VALUE) {
                return -1;
            }
            totalCost += minCost.get(s).get(t);
        }   
        return totalCost;
    }
    private Map<Character, Long> dijkstra(char start, Map<Character, List<int[]>> graph) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        Map<Character, Long> dist = new HashMap<>();     
        for (char ch = 'a'; ch <= 'z'; ch++) {
            dist.put(ch, Long.MAX_VALUE);
        }  
        dist.put(start, 0L);
        pq.offer(new int[] {start, 0});    
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            char currChar = (char) current[0];
            long currDist = current[1];      
            if (currDist > dist.get(currChar)) continue;     
            for (int[] neighbor : graph.get(currChar)) {
                char nextChar = (char) neighbor[0];
                long newDist = currDist + neighbor[1];         
                if (newDist < dist.get(nextChar)) {
                    dist.put(nextChar, newDist);
                    pq.offer(new int[] {nextChar, (int) newDist});
                }
            }
        }
        return dist;
    }
}
