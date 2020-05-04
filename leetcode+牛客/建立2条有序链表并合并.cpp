/*
@File    :   建立2条有序链表并合并.cpp
@Time    :   2020/03/27 11:34:19
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   c++/python版建立2条有序链表并合并.cpp
*/
/*
*/
#include <iostream>
#include <sstream>
using namespace std;
struct node
{
  int val;
  struct node *next;
};
node *create(string s)
{
  node *temp = new node, *head = temp;
  node *prev = head;
  stringstream ss;
  ss << s;
  int n;
  while (ss >> n)
  {
    temp->val = n;
    node *p = new node;
    prev = temp;
    temp->next = p;
    temp = p;
  }
  prev->next = NULL;
  // 因为建立的头结点也是有值的，链尾节点没用故删除
  delete temp;
  return head;
}
node *merge(node *one, node *two)
{
  node *res = new node, *head = res;
  node *prev = head;
  while (one != NULL && two != NULL)
  {
    int val = 0;
    if (one->val < two->val)
    {
      val = one->val;
      one = one->next;
    }
    else
    {
      val = two->val;
      two = two->next;
    }
    res->val = val;
    node *p = new node;
    prev = res;
    res->next = p;
    res = p;
  }
  prev->next = (one == NULL) ? two : one;
  delete res;
  return head;
}
void traverse(node *res)
{
  while (res != NULL)
  {
    cout << res->val << " ";
    res = res->next;
  }
}
int main()
{
  string s1, s2;
  getline(cin, s1);
  getline(cin, s2);
  node *one = create(s1);
  node *two = create(s2);
  node *res = merge(one, two);
  traverse(res);
  return 0;
}


// python

class node:
    def __init__(self, value=-1):
        self.val = value
        self.next = None


def create(s):
    p = node()
    head = p
    for i in s.split(" "):
        n = node(int(i))
        p.next = n
        p = n
    return head


def merge(one, two):
    res = node()
    head = res
    while one.next and two.next:
        val = 0
        p1, p2 = one.next, two.next
        if p1.val < p2.val:
            val = p1.val
            one = one.next
        else:
            val = p2.val
            two = two.next
        p = node(val)
        res.next = p
        res = p
    res.next = one.next if one.next else two.next
    return head


def seeMe(n):
    while n.next:
        print(n.next.val, end=" ")
        n = n.next


s1, s2 = input(), input()
one, two = create(s1), create(s2)
res = merge(one, two)
seeMe(res)
