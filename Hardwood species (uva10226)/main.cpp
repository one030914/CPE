#include <iomanip>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
  bool flag = false;
  int n = 0, total = 0;
  string name = "";
  map<string, double> tree;
  map<string, double>::iterator iter;

  cin >> n;
  cin.ignore();
  cin.ignore();
  while (n--) {
    if (flag) cout << "\n";

    flag = true;
    while (getline(cin, name) && name != "") {
      tree[name]++;
      total++;
    }
    for (iter = tree.begin(); iter != tree.end(); iter++) {
      cout << iter->first << " " << fixed << setprecision(4)
        << iter->second / total * 100 << endl;
    }
    tree.clear();
    total = 0;
  }

  return 0;
}