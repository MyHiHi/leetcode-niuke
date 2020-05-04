/*
@File    :   数组的众数.cpp
@Time    :   2020/04/03 11:14:28
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   数组的众数.cpp
*/
/*
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    vector<int> nums;
    while (getchar()!=']'){
        int c;
        cin>>c;
        nums.push_back(c);
    }
    sort(nums.begin(),end(nums));
    cout<< nums[nums.size()/2];
    return 0;
}
// python
nums=list(map(int,input().strip('[|]').split(',')));
p={};
ma=0;
l=len(nums)//2
for i in nums:
    p[i]=p.get(i,0)+1;
    if p[i]>l:
        print(i);
        break;