# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 示例:
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
def restoreIpAddresses(s: str):
    res=[];
    def backstr(s,tmp):
        if not s and len(tmp)==4:
            res.append('.'.join(tmp));
        elif len(tmp)<4:
            for i in range(min(3,len(s))):
                p,n=s[:i+1],s[i+1:];                
                if p and 0<=int(p)<=255 and str(int(p))==p:
                    backstr(n,tmp+[p]);
    backstr(s,[]);
    return res;

s="25525515"
print(restoreIpAddresses(s));
# ['2.55.255.15', '25.5.255.15', '25.52.55.15',
#   '255.2.55.15', '255.25.5.15', '255.25.51.5', '255.255.1.5']