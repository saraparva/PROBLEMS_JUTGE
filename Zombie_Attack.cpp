#include <iostream>
using namespace std;
int main(){
    int population, zombies=1, days=0;
    cin>>population;
    while(population>0){
        population-=2*zombies;
        if(population>0){
            zombies+=2*zombies;
            zombies-=0.25*zombies;
            population++;
            days++;
        }
        else{break;}
    }
    cout<<days<<" days"<<endl;
}
