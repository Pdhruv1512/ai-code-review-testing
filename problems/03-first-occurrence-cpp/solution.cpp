#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    while (q--) {
        int x;
        cin >> x;

        auto it = lower_bound(a.begin(), a.end(), x);

        if (it != a.end() && *it == x) {
            cout << (it - a.begin()) << '\n';
        } else {
            cout << -1 << '\n';
        }
    }

    return 0;
}
