#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string line;
    getline(cin, line);

    istringstream iss(line);
    vector<string> words;
    string word;

    while (iss >> word) {
        words.push_back(word);
    }

    for (int i = static_cast<int>(words.size()) - 1; i >= 0; --i) {
        if (i != static_cast<int>(words.size()) - 1) {
            cout << ' ';
        }
        cout << words[i];
    }

    cout << '\n';
    return 0;
}
