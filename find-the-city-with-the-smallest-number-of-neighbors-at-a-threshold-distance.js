var findTheCity = function(n, edges, distanceThreshold) {
    let dist = Array.from({ length: n }, () => Array(n).fill(Infinity));
    for (let i = 0; i < n; i++) {
        dist[i][i] = 0;
    }
    for (let [from, to, weight] of edges) {
        dist[from][to] = weight;
        dist[to][from] = weight;
    }
    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    let minReachable = Infinity;
    let resultCity = -1;
    for (let i = 0; i < n; i++) {
        let reachableCount = 0;
        for (let j = 0; j < n; j++) {
            if (dist[i][j] <= distanceThreshold) {
                reachableCount++;
            }
        }
        if (reachableCount <= minReachable) {
            minReachable = reachableCount;
            resultCity = i;
        }
    }   
    return resultCity;
};
