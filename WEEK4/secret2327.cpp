class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        const int modulo = 1e9 + 7; // modulo 10^9 + 7
        vector<long long> secret(n + 1, 0);
        secret[1] = 1;  // day 1: one person knows the secret
        
        long long people = 0;  // people who can share
        
        for (int day = 2; day <= n; ++day) {
            // each person will share the secret with a new person every day, starting from delay days after discovering the secret
            if (day - delay >= 1)
                people = (people + secret[day - delay]) % modulo;
            // People who forget secret and cannot share the secret
            if (day - forget >= 1)
                people = (people - secret[day - forget] + modulo) % modulo;
            
            secret[day] = people;  // people being shared the secret now
        }
        
        // people who still remember the secret by specific day n
        long long answer = 0;
        for (int i = 1 + n - forget; i <= n; ++i) {
            if (i >= 1) answer = (answer + secret[i]) % modulo;
        }
        
        return answer;
    }
};