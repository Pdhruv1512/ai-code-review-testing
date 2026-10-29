#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<long long, long long>> intervals(n);

    for (int i = 0; i < n; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    if (n == 0) {
        return 0;
    }

    sort(intervals.begin(), intervals.end());

    long long l = intervals[0].first;
    long long r = intervals[0].second;

    for (int i = 1; i < n; ++i) {
        if (intervals[i].first <= r) {
            // Overlapping intervals: extend the current interval.
            r = max(r, intervals[i].second);
        } else {
            // No overlap: output the current merged interval.
            cout << l << ' ' << r << '\n';
            l = intervals[i].first;
            r = intervals[i].second;
        }
    }

    // Output the final merged interval.
    cout << l << ' ' << r << '\n';

    return 0;
}
