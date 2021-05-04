# -*- UTF-8 -*-
import os
import sys
import time
import ctypes
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


def post(_url: str, _data: dict, _headers: dict = None):
    """Simple post

    Args:
        _url (str): url.
        _data (dict): data.
        _headers (dict): headers.

    Returns:
        <class 'requests.models.Response'>

    """

    return requests.post(_url,data=_data)


def sc_post(_data:dict):
    """Server酱|post https://sct.ftqq.com/

    Args:
        _data (dict): data.

    Returns:
        <class 'requests.models.Response'>
        
    """
    send_key=Secrets.send_key
    url="https://sctapi.ftqq.com/{0}.send".format(send_key)
    return post(url,_data)

def main():
    _data={"title":"test2","desp":"content"}
    r=sc_post(_data)
    print(r.text)
    print(type(r))
    


if __name__=="__main__":
    main()