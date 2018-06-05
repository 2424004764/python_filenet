import os, sys,time,re,pyautogui,win32api,win32con
sys.path.append(os.getcwd()+os.sep +'func.py')
sys.path.append(os.getcwd()+os.sep +'helpr.py')
import func,helpr
from ctypes import *

def main(command):
    #显示当前目录下的所有文件、文件夹信息
        if command == 'dir':
            func.show_the_dir_file()
            return False

        if command == 'cd':
            #如果输入cd，则不切换目录
            os.chdir('./')
            return False

        #切换到上一级
        if command =='cd ../':
            pat = re.compile(r'.*')#获取查找结果
            res1 = pat.findall(command,3,6)#查找字符串第3到第6个字符
            os.chdir(res1[0])
            return False

        #删除文件和文件夹
        if command == 'del':
            func.del_file_dir()
            return False
        # 删除文件和文件夹 e


        #显示帮助文档
        if command == 'help':
            for v,k in helpr.help.items():
                print('命令：'+v+'    '+k)

        #执行一个字符串表达式，并返回表达式的值
        if command == 'eval':
            func.python_()

        #进入系统命令模式，相当于cmd
        if command == 'winver':
            func.winver_()

        #输出作者信息
        if command == 'author':
            print(helpr.author)

        #关闭显示器
        if command == 'close_display':
            kuser = windll.user32
            wm_syscommand = 0x0112
            sc_monitorpower = 0xf170
            HWND_BROADCAST = kuser.FindWindowExA(None, None, None, None)
            kuser.SendMessageA(HWND_BROADCAST, wm_syscommand, sc_monitorpower, 2)

        #显示已完成的函数
        if command == 'finish_function':
            for v,k in helpr.finish_function.items():
                print('命令：'+v+'    '+k)

        #测试方法
        if command =='test':
            # print('关闭显示器')
            # # print(win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 1))
            #
            # kuser = windll.user32
            #
            # wm_syscommand = 0x0112
            # sc_monitorpower = 0xf170
            # HWND_BROADCAST = kuser.FindWindowExA(None, None, None, None)
            #
            # kuser.SendMessageA(HWND_BROADCAST, wm_syscommand, sc_monitorpower, 2)
            #
            # cur_position = pyautogui.position()#类型为元祖，通过下标访问
            # cur_x = cur_position[0]
            # cur_y = cur_position[1]
            # while 1:
            #     cur_position = pyautogui.position()  # 当前鼠标位置坐标 类型为元祖，通过下标访问
            #     x_y = 200  #当前鼠标移动的位置与坐标之间的间隙
            #     if cur_x-cur_position[0] >= x_y
            #     or cur_position[0]-cur_x >= x_y
            #     or cur_y-cur_position[1] >= x_y
            #     or cur_position[1]-cur_y >= x_y:
            #         print(cur_position)
            #         break
            # print('开启显示器')
            exec('print(\'666\')')

        #显示时间
        if command == 'time':
            print(func.return_time("%Y-%m-%d %H:%M:%S week:%w ")+str(int(time.time())))
            return False

        #退出程序
        if command == 'exit' or command == 'quit' :
            print('Bye')
            sys.exit()
