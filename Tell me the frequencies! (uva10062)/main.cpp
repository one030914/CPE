#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    string line;
    bool first = true;

    while (getline(cin, line)) {
        if (!first) cout << "\n";
        first = false;

        map<char, int> freq;

        for (char ch : line) {
            freq[ch]++;
        }

        vector<pair<int, char>> sorted_freq;
        for (auto &p : freq) {
            sorted_freq.push_back({ p.second, p.first });
        }

        sort(sorted_freq.begin(), sorted_freq.end(), [](const pair<int, char> &a, const pair<int, char> &b) {
            if (a.first != b.first)
                return a.first < b.first;
            return a.second > b.second;
        });

        for (auto &p : sorted_freq) {
            cout << (int)p.second << " " << p.first << "\n";
        }
    }

    return 0;
}
