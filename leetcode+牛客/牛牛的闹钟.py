# -*- encoding: utf-8 -*-
'''
@File    :   牛牛的闹钟.py
@Time    :   2020/02/08 11:41:52
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
目描述
牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
数据保证至少有一个闹钟可以让牛牛及时到达教室。
输出描述:
输出两个整数表示牛牛最晚起床时间。
示例1
输入
3 
5 0 
6 0 
7 0 
59 
6 59
输出
6 0
'''
import sys
lines=sys.stdin.readlines();
lines=[line.strip() for line in lines];
n=int(lines[0]);
clocks={};
for i in range(1,n+1):
    r=lines[i]
    c=list(map(int,r.split()));
    clocks[r]=c[0]*60+c[1];
delay=int(lines[-2]);
time=list(map(int,lines[-1].split()));
time=time[0]*60+time[1];
res="";
clocks=sorted(clocks.items(),key=lambda x:x[1],reverse=True);
f=time-delay;
for k,v in clocks:
    if v<=f:
        res=k;
        break;
print(res)
    