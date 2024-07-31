function maxPoints(points: number[][]): number {
    if (points.length === 1) {
        return 1;
    }
    let max = 2;
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            let tmp = 2;
            const s = (points[j][1] - points[i][1]);
            const r = points[i][1] * (points[j][0] - points[i][0]) - points[i][0] * s;

            if (points[j][0] !== points[i][0]) {
                for (let f = j + 1; f < points.length; f++) {
                    if (points[f][1] * (points[j][0] - points[i][0]) === s * points[f][0] + r) {
                        tmp++;
                    }
                }
            } else {
                 for (let f = j + 1; f < points.length; f++) {
                    if (points[f][0] === points[j][0]) {
                        tmp++;
                    }
                }
            }

            if (tmp > max) {
                max = tmp;
            }
        }
    }

    return max;
};
