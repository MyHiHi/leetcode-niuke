# -*- encoding: utf-8 -*-
'''
@File    :   reorderLogFiles.py
@Time    :   2020/02/06 10:12:45
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
有一个日志数组 logs。每条日志都是以空格分隔的字串。

对于每条日志，其第一个字为字母数字标识符。然后，要么：

标识符后面的每个字将仅由小写字母组成，或；
标识符后面的每个字将仅由数字组成。
我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。

将日志重新排序，使得所有字母日志都排在数字日志之前。
字母日志按内容字母顺序排序，忽略标识符；在内容相同时，按标识符排序。
数字日志应该按原来的顺序排列。

返回日志的最终顺序。

 

示例 ：

输入：["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


'''


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def r(log):
          # log=["aa 1 2 3 4 5"].split(" ",1)=["aa",["1 2 3 4 5"]]
            _id,rest=log.split(" ",1);
            # sorted从小到大排序，字母为0，数字为1，将字母日志排在数字日志之前
            # 然后按内容排序，相同时按标识符排序
            # 数字日志 得是元组 所以必须为(1,),不能为(1)
            return (0,rest,_id) if rest[0].isalpha() else (1,);
        return sorted(logs,key=r)