#include "iostream"
#include "math.h"
using namespace std;
int main(){
int a;
cin>>a;
int count=0;
for(int i =2;i<a;i++){
for(int j=2;j<i;j++){
for(int k=2;k<i;k++){
if(i%2==0 || i%3==0){

    if(pow(k,2)*pow(j,3)==i){
        //cout<<k<<" "<<j<<" "<<i;
        count++;
    }
}



}
}
}
cout<<count<<endl;
return 0;
}
