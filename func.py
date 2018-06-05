# -*- coding: utf-8 -*-
import time,os,re,shutil,_thread
import urllib.request#网络
import  sys,socket
sys.path.append(os.getcwd()+os.sep +'helpr.py')#导入帮助文件包
sys.path.append(os.getcwd()+os.sep +'thread_f.py')#导入线程包

import helpr,thread_f


#导入文件

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  #改变输出的标准编码


#将时间戳转换为时间组
def time_transition_timestamp(timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

#获取文件大小
def get_file_size(filename):
    stainfo = os.stat(filename)
    file_size = stainfo.st_size
    return byty_transition_memory(file_size)

#将字节转换为MB、GB等
def byty_transition_memory(file_size):
    if file_size < 1024:
        return str(file_size)+'byte'
    elif 1024 <= file_size < (1024**2):
        return str(round(file_size/1024,2)) + "KB"
    elif (1024**2) <= file_size < (1024**3):
        return str(round(file_size/(1024**2),2)) + 'MB'
    elif (1024**3) <= file_size < (1024**4):
        return str(round(file_size/(1024*1024*1024),2)) + 'GB'
    elif (1024**4) <= file_size < (1024**5):
        return str(round(file_size/(1024*1024*1024*1024))) + 'TB'
    elif (1024**5) <= file_size < (1024**6):
        return str(round(file_size/(1024**5))) + 'PB'
    return file_size #如果文件小于1024字节

#显示当前目录下的文件、文件夹信息
def show_the_dir_file():
    at_cd = os.getcwd()  # 显示当前工作目录
    dirs = os.listdir(at_cd)  # 获取文件夹下所有文件和文件夹的列表
    print('\n')#输出换行
    print('文件创建时间           类型     占用内存    文件名')
    file_num = 0 #定义文件数量总和变量
    dir_num = 0 #定义文件夹数量总和变量
    file_size = 0 #定义当前文件夹下所有文件的大小
    dir_size = 0 #定义当前文件夹下所有文件夹的大小总和
    for file in dirs:
        filename = at_cd + os.sep + file  # 拼接目录和文件名
        stinfo = os.stat(filename)
        file_time = time_transition_timestamp(stinfo.st_atime)  # 将时间戳转换为时间组
        file_size = get_file_size(filename)  # 获取文件大小
        if os.path.isdir(filename):  # 如果是文件夹,计算文件夹下各文件大小总和
            dir_or_file = '文件夹'
            dir_name = filename#获取当前文件夹名字
            dir_num += 1 #定义的变量自增
            try:
                file_size = get_dir_size(dir_name)
            except Exception as e:
                print(file + e)#输出错误信息
        elif os.path.isfile(filename): #如果是文件
            file_num += 1 #定义的变量自增1
            dir_or_file = '文件'
        print(file_time + "    " + dir_or_file + "     " + str(file_size) + "        " + file)  # 输出时间和文件名
    print('\t有个'+str(file_num)+'文件，'+str(dir_num)+'个文件夹')
    print('\n')#输出换行


#返回某一目录的大小，考虑到文件夹下，还可能有文件夹，伤脑筋
def get_dir_size(dir_name):#参数为文件夹名字
    size = 0
    dirs = os.listdir(dir_name)
    for file_name in dirs:
        stainfo = os.stat(dir_name+os.sep+file_name)
        size += stainfo.st_size
    return byty_transition_memory(size)

#切换到指定目录，检测切换字符串是否为正确格式
def switch_chdir(command):
    pat = re.compile(r'.*')#设置正则表达式
    res = pat.findall(command, 3, )#查找输入的字符串
    if len(res[0])==0:
        return False
    elif len(res[0]) >1:
        return res[0]

#删除文件或文件夹
def del_file_dir():
        at_cd = os.getcwd()  # 获取当前工作目录
        dirs = os.listdir(at_cd)  # 遍历目录
        i=0#声明函数全局变量
        dict = []#声明存放文件名的列表
        for filename in dirs:
            if os.path.isdir(filename):
                class1 = '文件夹  '
            elif os.path.isfile(filename):
                class1 = '文件    '
            print(str(i+1)+ '.'+ class1 +'    '+filename + '\t'+get_file_size(filename))
            i += 1
            dict.append(filename)
        del_num = input('请输入你要删除的文件序号(输入q退出)：>')
        # 如果直接按下回车
        if len(del_num)==0:
            del_file_dir()
        elif del_num == 'q':#如果按下输入q
            print(at_cd)#则显示当前目录名
        else:
            #删除文件夹
            try:
                if os.path.isdir(at_cd+os.sep+dict[int(del_num)-1]):
                    shutil.rmtree(at_cd+os.sep+dict[int(del_num)-1])
                    y_or_n = input('删除成功！输入Y继续删除，输入N退出>')
                    if y_or_n == 'y':
                        del_file_dir()
                    elif y_or_n == 'n':
                        return False
                    else:
                        del_file_dir()
            except Exception as e:
                print(e)

            # print(at_cd+'\\'+dict[0])
            try:#如果下面代码执行出错
                os.remove(dirs[int(del_num)-1])
            except (FileNotFoundError,ValueError,PermissionError,IndexError):#错误机制
                print('删除失败！文件不存在或命令错误')
                # del_file_dir()
            else:#如果try执行没有出错
                y_or_n = input('删除成功！输入Y继续删除，输入N退出>')
                if y_or_n == 'y':
                    del_file_dir()
                elif y_or_n == 'n':
                    return False
                else:
                    del_file_dir()
            # os.remove(dict[del_int_um - 1])

#类似php的获取当前时间方法，时间格式2018-3-31 14:47:47
def return_time(par):
    return time.strftime(par, time.localtime(time.time()))

#重命名文件
def rename_file(cmd):
    if cmd == 'rename':
        print('假如你要修改1.txt为2.txt，格式为rename 1.txt 2.txt')
    elif cmd != 'rename':
        at_cd = os.getcwd()#取当前工作目录
        match = re.match(r'(rename) (.*) (.*)',cmd)#正则匹配要重命名的两个文件，随便检测一下是否是文件
        # print(match.group(2))
        # print(match.group(3))
        try :
            before_file_name = match.group(2)#要重命名的文件
        except (AttributeError):
            pass
        try:
            later_file_name = match.group(3)#重命名之后的文件
            os.path.exists(at_cd + os.sep + later_file_name)
        except (AttributeError):
            print('要修改的文件不存在')
            return  False
        else:
            #先检测语句是否正常
            if before_file_name:#检测是否输入before_file_name
                #再检测是否match.group(2)是否是当前目录下已存在的文件
                if os.path.exists(at_cd+os.sep+before_file_name):
                    #再检测重命名之后的文件是否已存在
                    if os.path.exists(at_cd+os.sep+later_file_name):
                        print('修改失败！请输入修改之后的文件名')
                    else:
                        os.renames(before_file_name,later_file_name)
                        print('修改成功！')
            elif before_file_name == later_file_name:
                print('修改未进行，要修改的名字和修改后的名字一样！')
        #检测要重命名的文件是否存在以及是否是文件
        #检测是否存在

#创建新文件夹新目录
def mkdir_(cmd):#参数为传过来的命令
    if cmd=='mkdir':
        print('请在mkdir后面接上你要创建的文件夹名')
        return False
    match = re.match(r'(mkdir)( )+(.*)',cmd)
    dir_name = match.group(3)
    # print(dir_name)
    #调用命令创建目录
    try:#如果try内出错
        if os.path.exists(dir_name):#检测文件夹是否存在，存在返回True
            print('文件夹已存在！')
            return False #如果已存在文件夹，则返回False，接收下一条while命令
        else:#如果不存在则创建目录
            os.mkdir(dir_name)
    except Exception as e: #记录出现原因
        print(e)#输出错误信息
    else:
        print('[*] create dir : '+dir_name+' success')

#获取网站源码
def get_site_code(cmd):
    cmd_list = cmd.split( )
    if '-u' in cmd_list and '-c' in cmd_list and  cmd_list[0]=='sitecode':
        # print(cmd_list)
        re_num = int(cmd_list[4]) #刷新网页的次数
        #计算for循环用时
        t0 = time.time()
        fiaus = 0#记录失败的次数
        for num in range(1,re_num+1):
            #错误处理
            try:
                status = urllib.request.urlopen(cmd_list[2]).status
                # if status==200:
                #     print( '[*]success' + '  次数: '+ str(num) + '  状态: ' +str(status))
                # else:
                #     print('[*]success'+' 状态：'+str(num))
                if status != 200:
                    fiaus += 1
            except Exception as e:
                print(e)
                return False
        t1 = time.time()
        print("[*]success 用时 {0:.3f} 秒。失败{1}次".format(t1-t0,fiaus))
    elif '-u' in cmd_list and '-f' in cmd_list and cmd_list[0] == 'sitecode' or '-show' in cmd_list:#将源码保存到本地-f参数指定的位置
        try:
            #cmd_list 为 以空格分割的参数命令列表
            url = cmd_list[2]
            souce = urllib.request.urlopen(url).read()
            souce_decode = souce.decode('UTF-8','ignore')
            #sitecode -u http://www.fologde.com -f fologde.txt
            if '-show' in cmd_list:
                print(souce_decode)#如果有参数show则显示源码
                wiret_file(cmd_list[4],souce_decode)#调用函数写入网站源码
            else:
                wiret_file(cmd_list[4],souce_decode)#调用函数写入网站源码
        except Exception as e:
            print(e)
    else:
        print('参数不全或参数错误！请输入help sitecode显示帮助信息')

#获取某个命令的详情用法参数
def get_help_cmd(cmd):
    cmd_list = cmd.split() #分割，默认以空格分割字符串
    # print(cmd_list)
    # print(cmd_list[1])
    # print(helpr.sitecode)
    if len(cmd_list) <= 1:
        print('缺少参数！')
        return False
    try:
        if cmd_list[1] == 'sitecode':#如果查询sitecode帮助信息
            for v, k in helpr.sitecode.items():
                print(v + '    ' + k)
        #在这条注释下面添加其他if
        elif cmd_list[1] == 'finish_function':#如果查询finish_function帮助信息
            for v, k in helpr.finish_function.items():
                print(v + '    ' + k)
        else:
            print('无该命令！')
    except Exception as e:
        print(e)

#写入文件
#par str file_name  要写入的文件名
#par content 要写入的内容
#par way  写入方式  例："w":写入模式（覆盖）无此文件时自动创建
def wiret_file(file_name,content,way='w+'):
    try:
        with open(file_name, way, encoding='utf-8') as txt:
            txt.write(content + '\n\n')
        print('[*]get success!  文件地址：' + os.getcwd() + os.sep + file_name)
    except Exception as e:
        print(e)

#进入python解析器模式  执行一个字符串表达式，并返回表达式的值
def python_():
    print('已进入字符串解析模式模式  将返回表达式的值')
    print('input quit exit:')
    while True:
        command = input(">>")
        if command == 'quit':
            print('已退出字符串解析模式')
            break
        try:
            print(eval(command))
        except Exception as e:
            print(e)


#进入系统命令模式，相当于cmd
def winver_():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变输出的标准编码
    print('已进入系统命令模式  可执行cmd命令')
    print('input quit exit:')
    while True:
        command = input('cmd 模式'+os.getcwd()+">")
        if command == 'exit':
            print('已退出cmd模式')
            break
        try:
            print(os.system(command))
        except Exception as e:
            print(e)

#可不进入eval模式即可通过参数形式执行eval命令
def use_eval(cmd):
    cmd_list = cmd.split()  #分割字符串
    if len(cmd_list) == 2 and cmd_list[0] =='eval' :#判断分割的命令长度是否为二
        try:
            eval_cmd = cmd_list[1]#将字符串分离出来
            # print(eval_cmd)
            print(eval(eval_cmd))#输出eval函数执行结果
        except Exception as e:#记录错误信息
            print(e)#输出错误信息

#可不进入系统命令模式即可通过参数形式执行cmd命令
def use_cmd(cmd):
    cmd_list = cmd.split()  #分割字符串
    if len(cmd_list) >= 2 and cmd_list[0] =='cmd' :#判断分割的命令长度是否为二
        try:
            eval_cmd_list = cmd_list[1:]#将字符串分离出来
            # print(len(eval_cmd_list))
            # print(eval_cmd_list)
            eval_cmd = ''
            for va in range(0,len(eval_cmd_list)):
                eval_cmd += eval_cmd_list[va] + ' '
            # print(eval_cmd)
            print(os.system(eval_cmd))#输出eval函数执行结果
        except Exception as e:#记录错误信息
            print(e)#输出错误信息

#将域名转换为ip
def getdomainip(cmd):
    cmd_list = cmd.split()  #分割字符串
    if len(cmd_list)==1 : #判断输入的参数个数是否是一个
        print('缺少域名参数')
        return False
    try:
        if 'http://' in cmd_list[1]:#将输入的http://删除 下面的https://同理，因为下面获取域名ip不需要协议名，加了协议名反而报错
            cmd_list[1] = cmd_list[1].lstrip('http://')
        elif 'https://' in cmd_list[1]:
            cmd_list[1] = cmd_list[1].lstrip('https://')
        print(socket.gethostbyname(cmd_list[1]))
    except Exception as e:
        print(e)


#执行任意python代码
def exec_python(command):
    cmd_list = command.split()  # 分割字符串
    if len(cmd_list) >= 2 and cmd_list[0] == 'exec':  # 判断分割的命令长度是否为二
        try:
            # eval_cmd = cmd_list[1]  # 将字符串分离出来
            eval_cmd = ''
            for v in range(1,len(cmd_list)):
                eval_cmd = eval_cmd + cmd_list[v] + ' '
            # print(eval_cmd)
            print(exec(eval_cmd))   #执行python语句或代码  exec函数永远返回none
        except Exception as e:  # 记录错误信息
            print(e)  # 输出错误信息

#生成、创建一个文件
def create_file(com):
    cmd_list = com.split()  # 分割字符串
    # print(cmd_list[1])
    if len(cmd_list) == 1:
        print('请输入要创建的文件名，格式 ：touch info.txt')

    if len(cmd_list) >2 :
        print('你输入的参数有点多，作者还没想好怎么处理,正确格式 ：touch info.txt')

    try:
        with open(cmd_list[1], 'w', encoding='utf-8') as txt:
            txt.write('')
        print('[*]get success!  文件地址：' + os.getcwd() + os.sep + cmd_list[1])
    except Exception as e:
        print(e)