class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n, 0);
        stack<int> unresolved_ds;  // indices of unresolved days

        for (int i = 0; i < n; ++i) {
            // temp > temp at stack top
            while (!unresolved_ds.empty() && temperatures[i] > temperatures[unresolved_ds.top()]) {
                int prev_i = unresolved_ds.top();
                unresolved_ds.pop();
                result[prev_i] = i - prev_i;  // days waited
            }
            unresolved_ds.push(i);
        }

        return result;
    }
};