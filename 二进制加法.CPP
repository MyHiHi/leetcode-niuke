/*
@File    :   二进制加法.CPP
@Time    :   2020/03/30 11:36:14
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   二进制加法.CPP
*/
/*
*/ 
#include <iostream>
#include <string>
using namespace std;
int main(){
    string s1,s2,ans="";
    cin>>s1>>s2;
    int idx=0,l1=s1.size()-1,l2=s2.size()-1;
    while (l1>=0 || l2>=0){
        int c1=l1>=0?s1[l1]-'0':0,c2=l2>=0?s2[l2]-'0':0;
        int p=c1+c2;
        if (p==2){
            if (p+idx==3){
                ans="1"+ans;
            }else{
                ans="0"+ans;
            }
            idx=1;       
        }
        else if (p==1){
            if (p+idx==2){
                ans="0"+ans;
                idx=1;
            }else{
                ans="1"+ans;
                idx=0;
            }
        }else{
            if(p+idx==1){
                ans="1"+ans;
            }else{
                ans="0"+ans;
            }
            idx=0;
        }
        l1--;
        l2--;
    }
    if (idx==1)
        ans="1"+ans;
    cout<<ans;
    return 0;
}