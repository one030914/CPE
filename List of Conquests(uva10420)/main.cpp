#include <iostream>
#include <map>
using namespace std;

int main(){
    map<string, int> count;
    map<string, int>::iterator iter;
    string first = "";
    char others[76] = {0};
    int n = 0;
    cin >> n;
    
    while(n--){
        cin >> first;
        count[first]++;
        cin.getline(others, 76);
    }
    for(iter = count.begin(); iter != count.end(); iter++){
        cout << iter->first << " ";
        cout << iter->second << endl;
    }

    return 0;
}