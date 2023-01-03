#include<iostream>
#include <stack>
using namespace std;
bool areBracketBalanced(string str){
    stack<char>temp;
    for(int i=0;i<str.length();i++){
        if(temp.empty()){
            temp.push(str[i]);
        }
        else if(temp.top()=='{' && str[i]=='}' || temp.top()=='[' && str[i]==']' || temp.top()=='(' && str[i]==')'){
            temp.pop();
        }
        else{
            temp.push(str[i]);
        }
    }
    if(temp.empty()){
        return true;
    }
    return false;
}
int main(){
    string str;
    cout<<"Enter string: ";
    cin>>str;
    if(areBracketBalanced(str)){
        cout<<"\nString are balanced.";
    }
    else{
        cout<<"\nString are not balanced.";
    }
    

    return 0;
}