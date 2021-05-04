# -*- UTF-8 -*-
import os
import sys
import time
import ctypes
import psutil
import requests

from my_secrets import Secrets


def invisible(_flag: bool) -> None:
    """Set console window invisible or not.

    Args:
        _flag (bool): True for hide the console window, 
            The window will still show for a while and
            then disappear.

    Returns:
        None.

    """

    if _flag:
        whnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)


def post(_url: str, _data: dict, _headers: dict = None) -> requests.models.Response:
    """Simple post

    Args:
        _url (str): url.
        _data (dict): data.
        _headers (dict): headers.

    Returns:
        <class 'requests.models.Response'>

    """
    return requests.post(_url, data=_data)


def sc_post(_data: dict) -> requests.models.Response:
    """ServerChan`s post https://sct.ftqq.com/

    Example:
        _data={"title":"test_title","desp":"test_content"}

    Args:
        _data (dict): data.

    Returns:
        <class 'requests.models.Response'>
            If post successfully, the return code should be 2xx,
            the Response.text should be {"code":0,"message":"","data":{"pushid":"114514","readkey":"1145141919810","error":"SUCCESS","errno":0}}

            You can use `pushid` and `readkey` to check the push status,
            more at https://sct.ftqq.com/sendkey
    """
    send_key = Secrets.send_key
    url = "https://sctapi.ftqq.com/{0}.send".format(send_key)
    return post(url, _data)


class POINT(ctypes.Structure):
    """Mouse postion class.
    """
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]


def _position():
    """Get current mouse position.

    Returns:
        a tuple of mouse position.

    """
    cursor = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)


def move_detect(interval=1) -> bool:
    """Does mouse move during the interval.

    Args:
        interval (float,int): detect interval.

    Returns:
        True for mouse moves, False for not moving.

    """
    _pos1 = _position()
    time.sleep(interval)
    _pos2 = _position()
    return False if _pos1 == _pos2 else True


def is_process_exist(process_name: str) -> bool:
    """Does the process exist or not

    Args:
        process_name (str): process name.

    Returns:
        bool: True for exists, False otherwise.

    """
    pl = psutil.pids()
    for pid in pl:
        try:
            if psutil.Process(pid).name() == process_name:
                return True
        except:
            pass
    return False

def log(path:str,file_name:str) ->None:
    """Generate logs in current work directory

    Example:
        >>> log("/log","log.txt")
        cwd: D:/test
        this will create D:/test/log/log.txt

    """

def main():
    _data = {"title": "test2", "desp": "content"}
    r = sc_post(_data)
    print(r.text)
    print(type(r))


if __name__ == "__main__":
    main()
