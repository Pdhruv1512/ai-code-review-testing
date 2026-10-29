#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    __int128 sum = 0;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        sum += x;
    }

    if (sum == 0) {
        cout << 0 << '\n';
        return 0;
    }

    string result;
    while (sum > 0) {
        result += char('0' + sum % 10);
        sum /= 10;
    }

    for (int i = result.size() - 1; i >= 0; --i) {
        cout << result[i];
    }
    cout << '\n';

    return 0;
}
