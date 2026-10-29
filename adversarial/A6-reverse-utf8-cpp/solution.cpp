#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string s;
    getline(cin, s);

    vector<string> characters;

    // Split the UTF-8 string into Unicode code points.
    for (size_t i = 0; i < s.size();) {
        unsigned char c = static_cast<unsigned char>(s[i]);

        size_t length;
        if ((c & 0x80) == 0x00) {
            length = 1;  // 1-byte character
        } else if ((c & 0xE0) == 0xC0) {
            length = 2;  // 2-byte character
        } else if ((c & 0xF0) == 0xE0) {
            length = 3;  // 3-byte character
        } else {
            length = 4;  // 4-byte character
        }

        characters.push_back(s.substr(i, length));
        i += length;
    }

    // Reverse the Unicode code points.
    reverse(characters.begin(), characters.end());

    // Print the reversed string.
    for (const string& ch : characters) {
        cout << ch;
    }
    cout << '\n';

    return 0;
}
