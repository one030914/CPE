#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n = 0, m = 0;
    while (cin >> n >> m) {
        int num = m;

        for (int i = 1; n > num && m > 1; i++) {
            num = pow(m, i);
        }

        if (num > n || m <= 1) {
            cout << "Boring!" << endl;
        } else {
            while (num > 0) {
                cout << num;
                if (num != 1) {
                    cout << " ";
                } else {
                    cout << endl;
                }
                num /= m;
            }
        }
    }

    return 0;
}