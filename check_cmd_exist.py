import os, sys,re
sys.path.append(os.getcwd()+os.sep +'func.py')
sys.path.append(os.getcwd()+os.sep +'helpr.py')
import func,helpr #加载自己写的包
import os

#如果目录没有在定义的命令列表里
def check_cmd_exist(command):
    if re.match(r'cd', command):  # 正则匹配cd
        pat = re.compile(r'.*')
        res1 = pat.findall(command, 3, 6)
        if res1[0] == '../':  # 切换到上一级
            os.chdir(res1[0])
        elif func.switch_chdir(command):  # cd切换到其他目录
            try:
                os.chdir(func.switch_chdir(command))
            except (FileNotFoundError, PermissionError):
                print('此文件夹下没有指定的目录！或者权限不足，系统拒绝访问')
        return False
    elif command == '':  # 如果直接按下回车，则继续执行下一次循环
        return False
    elif re.match(r'rename', command):  # 正则匹配重命名方法 重命名
        func.rename_file(command)  # 执行函数
        return False
    elif re.match(r'mkdir', command):  # 正则匹配重命名方法  创建目录
        func.mkdir_(command)  # 执行函数
        return False
    elif re.match(r'sitecode', command):  # 正则匹配重命名方法  网络相关
        func.get_site_code(command)  # 执行函数
        return False
    elif re.match(r'eval', command):  # 正则匹配  执行字符串解析模式，返回字符串的值
        func.use_eval(command)  # 执行函数
        return False
    elif re.match(r'cmd', command):  # 正则匹配  执行cmd命令
        func.use_cmd(command)  # 执行函数
        return False
    elif re.match(r'help', command):  # 获取某个命令的详情参数
        func.get_help_cmd(command)  # 执行函数 参数为命令
        return False
    elif re.match(r'ping', command):  # 将域名转换为ip
        func.getdomainip(command)  # 执行函数 参数为命令
        return False
    elif re.match(r'exec', command):  # 执行任意python代码
        func.exec_python(command)  # 执行函数 参数为命令
        return False
    elif re.match(r'touch', command):  # 执行任意python代码
        func.create_file(command)  # 执行函数 参数为命令
        return False
    print('无此命令！')
    return False
