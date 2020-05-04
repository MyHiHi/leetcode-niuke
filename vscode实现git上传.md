# 1.vscode配置
`Vscode usersettings："git.path": "D:\\software\\Git\\cmd\\git.exe"`

# 2.git init :
```python
.git/config:
加入：
[remote "origin"]
url= https://github.com/MyHiHi/myGraduateProject.git
fetch=+refs/heads/*:refs/remotes/origin/*
[branch "master"]
remote=origin
merge=refs/heads/master
[user]
email = 909535692@qq.com
name = MyHiHi
```

# 3.在进行步骤3之前需要先控制台上传试试：
需要先有文件：
```
git remote add origin git@github.com:linhbcode/first-test.git
git add .
git commit -m "updated"
git push origin master  -f
git push --set-upstream origin master -f
```
###### ok

> 在你第一次使用时点击推送或者执行上条push的命令时会弹出github的登入框，输入用户名密码（在vscode中每次push都要输入用户名密码，这里可以执行git命令让git软件记住密码）如下：
在当前目录下输入：
`git config --global credential.helper store`