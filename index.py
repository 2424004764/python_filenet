# -*- coding: UTF-8 -*-
#time 2018-3-29 21:56:16
#@author 王茂成
#os.sep 获取系统路径间隔符号  window ->\    linux ->/

import os, sys,win32api
sys.path.append(os.getcwd()+os.sep +'func.py')
sys.path.append(os.getcwd()+os.sep +'helpr.py')
sys.path.append(os.getcwd()+os.sep +'check_cmd_exist.py')
sys.path.append(os.getcwd()+os.sep +'exec_command.py')
import func,helpr,check_cmd_exist,exec_command  #加载自己写的包

def main():
    getUserName = win32api.GetUserName()#调用系统api获取当前window用户名字
    soft_name = 'fileNet'#定义软件名字
    os.system('title '+soft_name)#设置标题
    os.system('color 0e')
    print('欢迎你：{0}!  {1}提示你：可输入help显示帮助信息！'.format(getUserName,soft_name))

    #输出永无bug提示
    print(helpr.forevel_not_bug)

    while 1:#无限循环，接收指令

        command = input(os.getcwd()+">>") #程序入口

        #检测是否存在某条命令，如果输入没有定义的命令，则提示无该命令
        if command not in helpr.keys:#如果目录没有在定义的命令列表里
            check_cmd_exist.check_cmd_exist(command)
            continue

        #调用本地包执行简单命令
        exec_command.main(command)  #例如：输入time  则显示时间  输入shutdown 则直接关机

if __name__ == '__main__':
    main()