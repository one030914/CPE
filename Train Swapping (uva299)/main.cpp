#include <iostream>

using namespace std;

int countSwaps(int arr[], int n) {
    int swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                swaps++;
            }
        }
    }
    return swaps;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n = 1;
        cin >> n;
        int arr[n];

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        int result = countSwaps(arr, n);
        cout << "Optimal train swapping takes " << result << " swaps.\n";
    }

    return 0;
}
