#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target;
    cin >> n >> target;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    unordered_map<long long, int> firstIndex;
    firstIndex.reserve(2 * n + 1);
    firstIndex.max_load_factor(0.7);

    for (int j = 0; j < n; ++j) {
        long long complement = target - a[j];

        auto it = firstIndex.find(complement);
        if (it != firstIndex.end()) {
            cout << it->second << ' ' << j << '\n';
            return 0;
        }

        // Keep the earliest index for each value.
        if (firstIndex.find(a[j]) == firstIndex.end()) {
            firstIndex[a[j]] = j;
        }
    }

    cout << "-1 -1\n";
    return 0;
}
