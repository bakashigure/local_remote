import os
import sys
import psutil
import time
import ctypes
import multiprocessing

path = os.getcwd()
log_path=path+'/Hint/' +'daemon_log.txt'

def log(content):
    with open(log_path,'a') as f:
        content=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +" "+str(content)
        f.write(str(content))
    f.close()

def loop():
    time.sleep(2)
    pl = psutil.pids()
    try:
        for pid in pl:
            if psutil.Process(pid).name()== 'watch_dog.exe':
                return True
    except:
        log("pid not found\n")
    return False    



whnd=ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.ShowWindow(whnd, 0)    
ctypes.windll.kernel32.CloseHandle(whnd) 

print(path)
while(1):
    if loop()==False:
        os.popen(path+'/'+"watch_dog.exe")
        time.sleep(3)
        log("process exit.\n")





