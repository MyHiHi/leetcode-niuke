/*
@File    :   二分图判定.cpp
@Time    :   2020/04/16 17:20:17
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   二分图判定.cpp
*/
/*
*/
#include <iostream>
#include <vector>
using namespace std;
bool dfs(vector<int> * graphs,int *colors,int i,int s){
    colors[i]=s;
    for (auto a:graphs[i]){
        if (s==colors[a]) return false;
        if (colors[a]==0 && !dfs(graphs,colors,a,-s)) return false;
    }
    return true;
}
bool paint(vector<int>* graphs,int * colors,int n){
    for (int i=1;i<=n;i++)
        if (colors[i]==0 && !dfs(graphs,colors,i,1))
            return false;
    return true;
}
int main(){
    int n,m;
    cin>>n>>m; 
    vector<int> graphs[n+1];
    for (int i=0;i<m;i++){
        int s,t;
        cin>>s>>t;
        graphs[s].push_back(t);
        graphs[t].push_back(s);
    }
    int *colors=new int[n+1];
    if (paint(graphs,colors,n))
        cout<<"Yes";
    else 
        cout<<"No";
    return 0;
}

// python
//定义俩个集合
///左边放一种颜色顶点
///右边放另一种颜色顶点
//当一次输入时一个集合同时出现俩个顶点就不能形成二分图
n,m=list(map(int,input().split()))
def paint():
    n1,n2=[],[]
    for _ in range(m):
        a,b=list(map(int,input().split()))
        if ((b in n1 and  a in n1) or (b in n2 and a in n2) ):
            return False
        elif (a in n1):
            n2+=[b]
        elif (b in n1):
            n2+=[a]
        elif (a in n2):
            n1+=[b]
        elif (b in n2):
            n1+=[a]
        else:
            n1+=[a]
            n2+=[b]
    return True
if paint():
    print('Yes')
else:
    print('No')
    