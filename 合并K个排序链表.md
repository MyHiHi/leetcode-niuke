<center>

# <font color=#0099ff size=72>合并K个排序链表</font>

**updated：2020/04/26 16:27:20**;
**&nbsp; &nbsp;author:Zhang tao**
</center>

## 题目

> 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
```python
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
```
## 思路

> look

## 代码


> 代码一：将链表中数字全部取出，然后排序，重建链表
```c++
/**

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
       
        vector<int> p;
        for (ListNode* t: lists){
            while (t){
                p.push_back(t->val);
                t=t->next;
            }
            cout<<endl;
        }
        if (p.size()<1) return NULL;
        sort(p.begin(),p.end());
        ListNode* head=new ListNode(p[0]),*r=head;
        for (int t=1;t<p.size();t++){
            ListNode *c=new ListNode(p[t]);
            r->next=c;
            r=c;
        }
        r->next=NULL;
        return head;

    }
};
```

## 代码二

> 用一个变量 ans 来维护以及合并的链表，第 i 次循环把第 i 个链表和 ans 合并，答案保存到 ans 中
```c++
class Solution {
public:
//合并两个链表为有序链表
    ListNode* mergeTwoList(ListNode* a,ListNode* b){
        if (!a || !b) return a?a:b;
        ListNode head,*tail=&head;
        while (a && b){
            if (a->val<b->val){
                tail->next=a,a=a->next;
            }else{
                tail->next=b,b=b->next;
            }
            tail=tail->next;
        }
        tail->next=a?a:b;
        return head.next;
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* ans=NULL;
        for (ListNode* t:lists)
            ans=mergeTwoList(ans,t);
        return ans;
    }
};
```

## 代码三
> 分治合并

1. 将$k$个链表配对并将同一对中的链表合并;
2. 第一轮合并以后， $k$个链表被合并成了$\frac{k}{2}$个链表，平均长度为$\frac{2n}{k}$,然后是$\frac{k}{4}$,$\frac{k}{8}$个链表等等
3. 重复这一过程，直到我们得到了最终的有序链表。
![markdown](https://pic.leetcode-cn.com/6f70a6649d2192cf32af68500915d84b476aa34ec899f98766c038fc9cc54662-image.png "markdown")

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* a,ListNode*b){
        ListNode head,*tmp=&head;
        while (a && b){
            if (a->val<b->val){
                tmp->next=a,a=a->next;
            }else{
                tmp->next=b,b=b->next;
            }
            tmp=tmp->next;
        }
        tmp->next=a?a:b;
        return head.next;
    }
    ListNode* merge(vector<ListNode*>& lists,int l,int r){
        if (l>r) return NULL;
        if (l==r) return lists[l];
        int mid=(l+r)>>1;
        return mergeTwoLists(merge(lists,l,mid),merge(lists,mid+1,r));
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
       return merge(lists,0,lists.size()-1);
    }
};
```

## 代码四

> 优先队列（heap）
> 
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        heap = []
        # 首先 for 嵌套 while 就是将所有元素
        # 都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next

```