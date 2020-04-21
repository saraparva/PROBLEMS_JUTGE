#include <iostream>
using namespace std;
int main(){
    int n,num,i,div,comp=0;
    cin>>num;
    n=num;
    for(i=num;i>0;i--){
        div=num%i;
        if(div==0){
            comp++;}
    }
    if (comp>2){
        cout<<n<<" is not prime"<<endl;}
    else{
        cout<<n<<" is prime"<<endl;}
}
