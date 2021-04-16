# -*- UTF-8 -*-
import os
import sys
import time

import win32api
import win32con
import win32gui
import win32ui
import ctypes

'''
whnd=ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.ShowWindow(whnd, 0)    
ctypes.windll.kernel32.CloseHandle(whnd) 
'''
detect_interval = 1

path = os.getcwd()


def isAlive() -> bool:
    hwnd_title={}
    def getAllHwnd(hwnd, mouse):
        if (
            win32gui.IsWindow(hwnd)
        ):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
    win32gui.EnumWindows(getAllHwnd, 0)
    for _, v in hwnd_title.items():
        # print(v,"\n")
        if v == "开源矿工挖矿端":
            return True
    else:
        return False


try:
    print("start in 5s")
    time.sleep(2)

    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long),
                    ("y", ctypes.c_long)]

    def position():
        cursor = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
        return (cursor.x, cursor.y)

    while(True):
        isMove = False
        time.sleep(detect_interval)
        pos1 = position()
        print("pos1: ", pos1,)
        time.sleep(detect_interval)
        pos2 = position()
        print("pos2: ", pos2)
        if pos1 == pos2:
            print("not moving, sleep\n")
        else:
            isMove = True
            print("detect moving!\n")
        # time.sleep(detect_interval)
        # hwnd_title={}
        exit_count = 0 # try 10 times
        if isMove:
            while(isAlive()):
                kill_process = os.popen("taskkill -im 开源矿工.exe", 'r')
                log = kill_process.read()
                print(log)
                print("try to kill..")
                if len(log) == 0:
                    continue
                else:
                    break
                #os.system("taskkill -im 开源矿工.exe")
                log_path = path+"/log.txt"
                with open(log_path, 'a') as f:
                    f.write(str(log))
                f.close()
            os._exit(2)

            '''
            def getAllHwnd(hwnd, mouse):
                if (
                    win32gui.IsWindow(hwnd)
                ):
                    hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
            win32gui.EnumWindows(getAllHwnd, 0)
            for k,v in hwnd_title.items():
                #print(v,"\n")
                if v == "开源矿工挖矿端":
                    print("found!")
                    os.system("taskkill -im 开源矿工.exe")
                    time.sleep(detect_interval)
                    os.system("taskkill -im 开源矿工.exe")
                    os._exit(2)
            '''
        # print(hwnd_title)
    # os.system("pause")
except Exception as e:
    error_log_path = path+"/error.txt"
    with open(error_log_path, 'w') as f:
        f.write(str(e))
    f.close()
