初始化
git init

添加文件
git add . 

上传版本 
git commit -m "描述信息"

相当于 git add . 和 git commit -m 的简写
git commit -a 

添加管路员邮箱
git config --global user.email "我的邮箱"

添加管理员姓名
git config --global user.name "我的名字"

查看状态
git status 

查看版本日志（只能看当前版本前的日志）
git log	

查看所有的版本日志
git reflog

回滚版本
git reset --hard 版本号码

拉dev分支的代码
git pull origin dev 
    相当于  
        - git fetch origin dev + git merge origin dev 会导致出现分叉
        - git fetch origin dev + git rebase origin dev 不会出现分叉


上传到git 服务器代码托管
git push origin dev  



















