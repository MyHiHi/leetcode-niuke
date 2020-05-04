<center>

# <font color=#0099ff size=72>跳跃游戏 II</font>

**updated：2020/05/04 15:43:38**;
**&nbsp; &nbsp;author:Zhang tao**
</center>

## 题目

> 给定一个非负整数数组，你最初位于数组的第一个位置,数组中的每个元素代表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个位置。

```python
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
```

## 思路

> 这道题是典型的贪心算法，通过局部最优解得到全局最优解。以下两种方法都是使用贪心算法实现，只是贪心的策略不同，我们每次在可跳范围内选择可以使得跳的更远的位置。

## 代码

### 1.反向查找出发位置(只有Java代码不超时)

> 我们知道最终要到达最后一个位置，然后我们找前一个位置，遍历数组，找到能到达它的位置，离它最远的就是要找的位置。然后继续找上上个位置，最后到了第 0 个位置就结束了。至于离它最远的位置，其实我们从左到右遍历数组，第一个满足的位置就是我们要找的。
时间复杂度：$O(n²)$，因为最坏的情况比如11111，position 会从 5 更新到 0，并且每次更新都会经历一个 `for `循环。
```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        int index=nums.size()-1,step=0;
        while (index>0){
            for (int i=0;i<index;i++)
                if (nums[i]>=index-i){
                    index=i;
                    step++;
                    break;
                }
        }
        return step;
    }
};
```

### 2.正向查找可到达的最大位置

![](https://assets.leetcode-cn.com/solution-static/45/45_fig1.png)

> 时间复杂度:$O(n)$,空间复杂度:$O(1)$
```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        // maxPosition：可以跳的更远的下标，记为边界
        int i=0,end=0,maxPosition=0,step=0;
        // i不用到达末尾，开始的时候边界是第0个位置，steps 已经加1了，
        //如果最后一步刚好跳到了末尾，此时 steps 其实不用加1了，
        //测试用例为`[1,2]`,如果`i<=nums.size()-1`，step反而为2，多增加了1。
        while (i<nums.size()-1){
            // 维护当前能够到达的最大下标位置
            maxPosition=max(maxPosition,i+nums[i]);
            // 从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。
            if (i==end){
                end=maxPosition,step++;
            }
            i++;
        }
        return step;
    }
};
```
