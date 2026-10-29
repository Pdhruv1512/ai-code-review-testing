#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    cin >> n >> k;

    unordered_map<long long, long long> freq;
    freq.reserve(2 * n);
    freq.max_load_factor(0.7);

    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;

        long long r = ((x % k) + k) % k;
        long long need = (k - r) % k;

        auto it = freq.find(need);
        if (it != freq.end()) {
            ans += it->second;
        }

        ++freq[r];
    }

    cout << ans << '\n';
    return 0;
}
