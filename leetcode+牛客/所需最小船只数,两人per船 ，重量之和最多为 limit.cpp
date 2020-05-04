/*
@File    :   船 ，重量之和最多为 limit.cpp
@Time    :   2020/03/17 11:00:09
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   所需最小船只数,两人per船 ，重量之和最多为 limit.cpp
*/
/*
*/
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;
int main(){
    string s;
    getline(cin,s);
    int limit;
    int res=0;
    cin>>limit;
    stringstream ss;
    ss<<s;
    vector<int> d;
    int t;
    while(ss>>t)
        d.push_back(t);
    sort(d.begin(),d.end());
    int i=0,j=d.size()-1;
    while (i<=j){
        if (d[i]+d[j]<=limit){
            i++;
            j--;
        }else{
            j--;
        }
        res++;
    }
    cout<<res<<endl;
    return 0;
}
