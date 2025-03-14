#include <iostream>
#include <algorithm>
using namespace std;

int n = 0, m = 0;

bool cmp(int x, int y){
    int xOdd = abs(x % 2), yOdd = abs(y % 2);
    if(x % m != y % m) return x % m < y % m;
    else if(xOdd != yOdd) return xOdd > yOdd;
    else if(xOdd) return x > y;
    else return x < y;
}

int main(){
    int nums[10000] = {0};

    while(cin >> n >> m){
        cout << n << " " << m << endl;
        if(n == 0 || m == 0) break;
        for(int i = 0; i < n; i++){
            cin >> nums[i];
        }
        sort(nums, nums+n, cmp);
        for(int i = 0; i < n; i++){
            cout <<  nums[i] << endl;
        }
    }
}