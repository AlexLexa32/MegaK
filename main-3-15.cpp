#include <iostream>
#include <string>
using namespace std;
int main()
{
    int q, w;
    q = 0;
    w = 0;
    
    char s;
    
   while(true){
       cin>>q>>s>>w;
       
    switch(s){
    case '*':
       cout<<w*q;
       break;
        
    case '/':
       cout<<q/w;
       break;
        
    case '-':
       cout<<q-w;
       break;
        
    case '+':
       cout<<w+q;
       break;
       
       case '!':
       return 0;
       
       default:
        return 0;
    }
    cin.get();
    
}
}