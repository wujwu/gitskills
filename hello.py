import time

'''
合并模式：
Fast-forward：直接把master指向dev的当前提交，所以合并速度非常快。
当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。
解决冲突就是把Git合并失败的文件手动编辑为我们希望的内容，再提交。
'''
