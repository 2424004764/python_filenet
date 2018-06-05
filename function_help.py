'''
需要导入相应包
win32api.keybd_event(13, 0, 0, 0)  # enter
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
'''