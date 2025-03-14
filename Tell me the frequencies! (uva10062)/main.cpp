#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int main(){
    map<int, int> ans;
    bool flag = false;
    string str;
    while(getline(cin, str)){
        if(flag) cout << "\n";
        flag = true;

        for(char i : str){
            ans[(int) i]++;
        }
        for(auto it : ans){
            sort(it.second.begin(), it.second.end());
            cout << it.first << " " << it.second << endl;
        }
    }
}