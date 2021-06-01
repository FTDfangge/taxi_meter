# 出租车计价系统

# 运行方式
直接运行main.py即可，或者运行生成的exe文件
# 代码结构
文件main.py为主函数，作用为调用菜单并运行

文件settings.py为设置参数，可以手动修改其中的参数，未做非法参数检测，所以需要开发者修改时注意，否则可能引起程序崩溃

文件record.txt为储存记录

文件夹services储存三种服务
1. file_operator.py 储存文件操作
2. menu.py 储存菜单
3. taxi_meter.py 为计价器