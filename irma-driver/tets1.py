#1.切换到开发分支git pull -r
#2.然后add commit，开发完之后，就push上远程，本地和远程同步了
#3.然后准备执行合并commmit，准备合并到正式环境
#4.git rebase -i HEAD~2
#5.如果有意外就git rebase --quit取消合并
#6.记录下来commit的id

#7.去到master，先git pull -r
#8.然后git cherry-pick comit的id
#9.然后git pr 吧，或者git push
