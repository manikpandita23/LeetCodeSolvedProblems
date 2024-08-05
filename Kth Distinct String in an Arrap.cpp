#include <vector>
#include <string>
#include <unordered_map>
using namespace std;
class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> freqMap;
        for (const auto& str : arr) {
            freqMap[str]++;
        }
        for (const auto& str : arr) {
            if (freqMap[str] == 1) {
                k--;
                if (k == 0) {
                    return str;
                }
            }
        } 
        return "";
    }
};
