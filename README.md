# RedisDirScan
此脚本用于测试 Rdies 未授权访问，在没权限写ssh私钥和定时任务又不知道web绝对路径的情况下，进行WEB目录探测

Python >= 3.x

需要安装 redis 库

\>pip install redis

替换 E:\\dirs.txt 为自己的字典，注意字符编码  报错很大几率是因为编码问题

rootPath 为开始爆破的根路径

### PS:此脚本是用来代替手动猜目录的，有没有用，还是靠字典！！！

![file](https://raw.githubusercontent.com/r35tart/RedisDirScan/master/redisDirScan.png)
