# -*- encoding: utf-8 -*-
'''
@File    :   dfs，单词组成句子.py
@Time    :   2020/03/25 15:53:21
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   dfs，单词组成句子.py
'''

'''
题目描述
Given a string s and a dictionary of words dict, add spaces in s 
to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

输入描述:
s ="catsanddog"
dict ="cat", "cats", "and", "sand", "dog"
输出描述:
[cats and dog, cat sand dog]
'''
# 80%
s=input().strip()
s=s[s.index('"')+1:-1];
dic=input().strip()
dic=eval("{"+dic[dic.index('"'):]+"}")
def dfs(s:str,dic:set,arr:list,res:list):
    if s=="":
        res+=[' '.join(arr)];
        return ;
    for k in dic:
        if s.startswith(k):
            dfs(s[len(k):],dic,arr+[k],res);
res=[]
dfs(s,dic,[],res);
print("["+','.join(res)+"]")