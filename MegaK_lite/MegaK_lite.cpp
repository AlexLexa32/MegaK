#include <iostream>
using namespace std;
int main() {
    int q, w;
    char s;
    cin >> q >> s >> w;
    switch(s){
        case '*':
           cout << w*q;
           break;
        case '/':
            cout << q/w;
           break;
        case '-':
            cout << q-w;
            break;
        case '+':
            cout << w+q;
            break;
        default:
            cout << w%q;
    }
}
